import streamlit as st
import pandas as pd
import folium
import os
from streamlit_folium import st_folium
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="IoT Vehicle Tracking Dashboard",
    page_icon="🚗",
    layout="wide"
)

# =====================================
# AUTO REFRESH
# =====================================
st_autorefresh(interval=5000, key="vehicle_dashboard")

# =====================================
# MAIN APP LOGIC
# =====================================
try:
    st.title("🚗 IoT Vehicle Tracking & Theft Prevention System")
    st.caption("Industry-Oriented Fleet Monitoring Dashboard")

    # LOAD DATA
    csv_file = None
    if os.path.exists("data/vehicle_log.csv"):
        csv_file = "data/vehicle_log.csv"
    elif os.path.exists("data/sample_vehicle_log.csv"):
        csv_file = "data/sample_vehicle_log.csv"

    if csv_file is None:
        df = pd.DataFrame({
            "timestamp": ["2025-06-12 10:00:00", "2025-06-12 10:01:00", "2025-06-12 10:02:00"],
            "latitude": [12.9716, 12.9720, 12.9730],
            "longitude": [77.5946, 77.5950, 77.5960],
            "status": ["MOVING", "MOVING", "MOVING"],
            "alert": ["NONE", "NONE", "NONE"]
        })
    else:
        df = pd.read_csv(csv_file)

    if len(df) == 0:
        st.warning("No vehicle data available.")
        st.stop()

    latest = df.iloc[-1]
    latitude = float(latest["latitude"])
    longitude = float(latest["longitude"])
    status = str(latest["status"])
    alert = str(latest["alert"])
    speed = 35

    # DASHBOARD CONTROLS
    st.subheader("⚙ Dashboard Controls")
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        if st.button("🔄 Refresh Dashboard", use_container_width=True):
            st.rerun()
    with c2:
        if st.button("🗑 Clear History", use_container_width=True):
            empty_df = pd.DataFrame(columns=["timestamp", "latitude", "longitude", "status", "alert"])
            os.makedirs("data", exist_ok=True)
            empty_df.to_csv("data/vehicle_log.csv", index=False)
            st.success("Vehicle History Cleared")
            st.rerun()
    with c3:
        st.download_button("📥 Download CSV", data=df.to_csv(index=False), file_name="vehicle_log.csv", mime="text/csv", use_container_width=True)
    with c4:
        st.info("Auto Refresh: 5 sec")

    st.divider()

    # SIDEBAR
    st.sidebar.title("Vehicle Details")
    st.sidebar.info("Vehicle ID : VH001\n\nDriver : Demo Driver\n\nMode : Simulation\n\nStatus : Active")
    st.sidebar.success("System Online")

    # KPI CARDS
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Latitude", round(latitude, 6))
    col2.metric("Longitude", round(longitude, 6))
    col3.metric("Speed", f"{speed} km/h")
    col4.metric("Status", status)
    if alert == "THEFT ALERT": col5.error(alert)
    elif alert == "GEOFENCE ALERT": col5.warning(alert)
    else: col5.success(alert)

    st.divider()

    # LIVE MAP
    st.subheader("📍 Live Vehicle Location")
    vehicle_map = folium.Map(location=[latitude, longitude], zoom_start=15)
    folium.Marker([latitude, longitude], popup="Vehicle Position", tooltip="Vehicle").add_to(vehicle_map)
    st_folium(vehicle_map, width=1200, height=500)
    
    st.link_button("🗺 Open in Google Maps", f"https://www.google.com/maps?q={latitude},{longitude}")

    # CHARTS
    chart1, chart2 = st.columns(2)
    with chart1:
        st.subheader("🚨 Alert Statistics")
        st.bar_chart(df["alert"].value_counts())
    with chart2:
        st.subheader("🚗 Vehicle Status Statistics")
        st.bar_chart(df["status"].value_counts())

    # HISTORY TABLES
    st.subheader("📊 Vehicle History")
    st.dataframe(df.tail(50), use_container_width=True)

    st.subheader("🚨 Recent Alerts")
    alerts = df[df["alert"] != "NONE"]
    if len(alerts) > 0:
        st.dataframe(alerts.tail(20), use_container_width=True)
    else:
        st.success("No alerts detected.")

    st.caption(f"Last Updated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

except Exception as e:
    st.error(f"Dashboard Error: {e}")