import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

st_autorefresh(
    interval=5000,
    key="vehicle_dashboard"
)
st.set_page_config(
    page_title="Vehicle Tracking Dashboard",
    page_icon="🚗",
    layout="wide"
)

# --------------------------------
# HEADER
# --------------------------------

st.title("🚗 IoT Vehicle Tracking & Theft Prevention System")
st.caption("Industry-Oriented Fleet Monitoring Dashboard")

# --------------------------------
# LOAD DATA
# --------------------------------

try:
    import os
    if os.path.exists("data/vehicle_log.csv"):
      df = pd.read_csv("data/vehicle_log.csv")

    elif os.path.exists("data/sample_vehicle_log.csv"):
     df = pd.read_csv("data/sample_vehicle_log.csv")
    df = pd.read_csv(csv_file)

    if len(df) == 0:
        st.warning("No vehicle data available.")
        st.stop()

    latest = df.iloc[-1]

    latitude = latest["latitude"]
    longitude = latest["longitude"]
    status = latest["status"]
    alert = latest["alert"]

    speed = 35

    # --------------------------------
    # SIDEBAR
    # --------------------------------

    st.sidebar.title("Vehicle Details")

    st.sidebar.info(
        """
        Vehicle ID : VH001
        
        Driver : Demo Driver
        
        Mode : Simulation
        
        Status : Active
        """
    )

    st.sidebar.success("System Online")

    # --------------------------------
    # KPI CARDS
    # --------------------------------

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Latitude",
        round(latitude, 6)
    )

    col2.metric(
        "Longitude",
        round(longitude, 6)
    )

    col3.metric(
        "Speed",
        f"{speed} km/h"
    )

    col4.metric(
        "Status",
        status
    )

    if alert == "THEFT ALERT":
        col5.error(alert)

    elif alert == "GEOFENCE ALERT":
        col5.warning(alert)

    else:
        col5.success(alert)

    st.divider()

    # --------------------------------
    # LIVE MAP
    # --------------------------------

    st.subheader("📍 Live Vehicle Location")

    vehicle_map = folium.Map(
        location=[latitude, longitude],
        zoom_start=15
    )

    folium.Marker(
        [latitude, longitude],
        popup="Vehicle Position",
        tooltip="Vehicle"
    ).add_to(vehicle_map)

    st_folium(
        vehicle_map,
        width=1200,
        height=500
    )

    maps_url = (
        f"https://maps.google.com/?q={latitude},{longitude}"
    )

    st.link_button(
        "🗺 Open in Google Maps",
        maps_url
    )

    st.divider()

    # --------------------------------
    # CHARTS
    # --------------------------------

    c1, c2 = st.columns(2)

    with c1:

        st.subheader("🚨 Alert Statistics")

        alert_stats = (
            df["alert"]
            .value_counts()
        )

        st.bar_chart(alert_stats)

    with c2:

        st.subheader("🚗 Vehicle Status")

        status_stats = (
            df["status"]
            .value_counts()
        )

        st.bar_chart(status_stats)

    st.divider()

    # --------------------------------
    # HISTORY TABLE
    # --------------------------------

    st.subheader("📊 Vehicle History")

    st.dataframe(
        df.tail(50),
        use_container_width=True
    )

    st.divider()

    # --------------------------------
    # ALERT HISTORY
    # --------------------------------

    st.subheader("🚨 Recent Alerts")

    alerts = df[
        df["alert"] != "NONE"
    ]

    if len(alerts) > 0:

        st.dataframe(
            alerts.tail(20),
            use_container_width=True
        )

    else:

        st.success(
            "No alerts detected."
        )

    st.divider()

    # --------------------------------
    # FOOTER
    # --------------------------------

    st.caption(
        f"Last Updated : {datetime.now()}"
    )

except Exception as e:

    st.error(
        f"Dashboard Error: {e}"
    )