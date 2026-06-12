import streamlit as st
import pandas as pd
import requests
import folium

from datetime import datetime
from streamlit_folium import st_folium
from streamlit_autorefresh import st_autorefresh

# ==================================
# CONFIG
# ==================================

CHANNEL_ID = "3406688"
READ_API_KEY = "LFWHS731QBFW62KQ"

st.set_page_config(
    page_title="IoT Vehicle Tracking Dashboard",
    page_icon="🚗",
    layout="wide"
)

# ==================================
# AUTO REFRESH
# ==================================

st_autorefresh(
    interval=5000,
    key="dashboard_refresh"
)

# ==================================
# HEADER
# ==================================

st.title(
    "🚗 IoT Vehicle Tracking & Theft Prevention System"
)

st.caption(
    "Industry-Oriented Fleet Monitoring Dashboard"
)

try:

    # ==================================
    # GET THINGSPEAK DATA
    # ==================================

    url = (
        f"https://api.thingspeak.com/channels/"
        f"{CHANNEL_ID}/feeds.json"
        f"?api_key={READ_API_KEY}"
        f"&results=50"
    )

    response = requests.get(
        url,
        timeout=10
    )

    data = response.json()

    feeds = data["feeds"]

    if len(feeds) == 0:
        st.warning(
            "No data received from ThingSpeak."
        )
        st.stop()

    rows = []

    for row in feeds:

        rows.append({

            "timestamp":
                row["created_at"],

            "latitude":
                row["field1"],

            "longitude":
                row["field2"],

            "status":
                row["field3"],

            "alert":
                row["field4"],

            "speed":
                row["field5"]

        })

    df = pd.DataFrame(rows)

    df["latitude"] = pd.to_numeric(
        df["latitude"],
        errors="coerce"
    )

    df["longitude"] = pd.to_numeric(
        df["longitude"],
        errors="coerce"
    )

    df["speed"] = pd.to_numeric(
        df["speed"],
        errors="coerce"
    )

    df = df.dropna()

    latest = df.iloc[-1]

    latitude = float(
        latest["latitude"]
    )

    longitude = float(
        latest["longitude"]
    )

    speed = int(
        latest["speed"]
    )

    status = str(
        latest["status"]
    )

    alert = str(
        latest["alert"]
    )

    # ==================================
    # SIDEBAR
    # ==================================

    st.sidebar.title(
        "Vehicle Details"
    )

    st.sidebar.info(
        f"""
Vehicle ID : VH001

Driver : Demo Driver

Mode : ThingSpeak Live

Status : Active
"""
    )

    st.sidebar.success(
        "🟢 ThingSpeak Connected"
    )

    # ==================================
    # DASHBOARD STATUS
    # ==================================

    st.success(
        f"Latest Record Time : {latest['timestamp']}"
    )

    # ==================================
    # KPI CARDS
    # ==================================

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric(
        "Latitude",
        round(latitude, 6)
    )

    c2.metric(
        "Longitude",
        round(longitude, 6)
    )

    c3.metric(
        "Speed",
        f"{speed} km/h"
    )

    c4.metric(
        "Status",
        status
    )

    if alert == "THEFT ALERT":

        c5.error(alert)

    elif alert == "GEOFENCE ALERT":

        c5.warning(alert)

    else:

        c5.success(alert)

    st.divider()

    # ==================================
    # LIVE MAP
    # ==================================

    st.subheader(
        "📍 Live Vehicle Location"
    )

    fmap = folium.Map(
        location=[
            latitude,
            longitude
        ],
        zoom_start=15
    )

    folium.Marker(
        [
            latitude,
            longitude
        ],
        popup="Vehicle",
        tooltip="Live Vehicle"
    ).add_to(fmap)

    st_folium(
        fmap,
        width=None,
        height=500
    )

    st.link_button(
        "🗺 Open In Google Maps",
        f"https://www.google.com/maps?q={latitude},{longitude}"
    )

    st.divider()

    # ==================================
    # CHARTS
    # ==================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "🚨 Alert Statistics"
        )

        st.bar_chart(
            df["alert"].value_counts()
        )

    with col2:

        st.subheader(
            "🚗 Status Statistics"
        )

        st.bar_chart(
            df["status"].value_counts()
        )

    st.divider()

    # ==================================
    # HISTORY
    # ==================================

    st.subheader(
        "📊 Vehicle History"
    )

    st.dataframe(
        df.tail(50),
        use_container_width=True
    )

    st.divider()

    # ==================================
    # ALERT HISTORY
    # ==================================

    st.subheader(
        "🚨 Recent Alerts"
    )

    alerts = df[
        df["alert"] != "NONE"
    ]

    if len(alerts):

        st.dataframe(
            alerts.tail(20),
            use_container_width=True
        )

    else:

        st.success(
            "No alerts detected."
        )

    st.divider()

    st.caption(
        f"Dashboard Updated : "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

except Exception as e:

    st.error(
        f"Dashboard Error : {e}"
    )