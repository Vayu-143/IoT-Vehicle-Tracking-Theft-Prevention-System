# 🚗 IoT Vehicle Tracking & Theft Prevention System

### Real-Time Vehicle Monitoring, Geofencing & Theft Detection using IoT, GPS Simulation, ThingSpeak Cloud, and Streamlit Dashboard

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![ThingSpeak](https://img.shields.io/badge/ThingSpeak-Cloud-orange)
![IoT](https://img.shields.io/badge/IoT-Vehicle%20Tracking-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📖 Overview

The **IoT Vehicle Tracking & Theft Prevention System** is an industry-oriented IoT project designed to provide real-time vehicle monitoring, GPS location tracking, geofencing alerts, theft detection, cloud connectivity, and interactive dashboard visualization.

The system simulates vehicle movement, uploads live GPS coordinates to the ThingSpeak IoT Cloud platform, and visualizes the data through a professional Streamlit dashboard.

This project demonstrates how modern IoT technologies can be used to improve vehicle security, fleet management, and asset tracking.

---

## 🌐 Live Dashboard

**Streamlit Dashboard**

https://iot-vehicle-tracking-theft-prevention-system-632ddnbtrfpp2pxfh.streamlit.app/

---

## 💻 GitHub Repository

https://github.com/Vayu-143/IoT-Vehicle-Tracking-Theft-Prevention-System

---

## ✨ Features

### 📍 Real-Time Vehicle Tracking

* Live GPS coordinate monitoring
* Dynamic vehicle location updates
* Interactive map visualization

### 🚨 Theft Detection

* Detects unauthorized vehicle movement
* Generates theft alerts
* Displays alert history

### 🛰 Geofencing

* Defines safe operating zones
* Detects boundary violations
* Generates geofence alerts

### ☁ ThingSpeak Cloud Integration

* Real-time IoT data upload
* Cloud-based vehicle monitoring
* Historical data storage

### 📊 Professional Dashboard

* Live vehicle status
* Speed monitoring
* Alert statistics
* Vehicle history table
* Google Maps integration

### 📄 Automated Reporting

* PDF report generation
* Alert logging
* Historical analysis

---

## 🏗 System Architecture

```text
GPS Simulator
      │
      ▼
Vehicle Data Generation
      │
      ▼
ThingSpeak IoT Cloud
      │
      ▼
Streamlit Dashboard
      │
      ▼
Real-Time Monitoring
```

---

## 🔧 Technology Stack

### Programming Languages

* Python

### IoT Platform

* ThingSpeak Cloud

### Dashboard

* Streamlit

### Mapping

* Folium
* Google Maps

### Data Processing

* Pandas

### Reporting

* ReportLab

### Visualization

* Streamlit Charts

---

## 📂 Project Structure

```text
IoT-Vehicle-Tracking-Theft-Prevention-System
│
├── arduino_code/
│
├── circuit_diagram/
│
├── dashboard/
│
├── data/
│   └── vehicle_log.csv
│
├── docs/
│
├── images/
│
├── outputs/
│   └── vehicle_report.pdf
│
├── python_simulation/
│   ├── __init__.py
│   ├── gps_simulator.py
│   ├── geofence.py
│   ├── logger.py
│   ├── pdf_report.py
│   └── thingspeak_sender.py
│
├── reports/
│
├── dashboard.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/Vayu-143/IoT-Vehicle-Tracking-Theft-Prevention-System.git

cd IoT-Vehicle-Tracking-Theft-Prevention-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project

### Step 1: Start GPS Simulation

```bash
python main.py
```

or

```bash
python python_simulation/gps_simulator.py
```

---

### Step 2: Launch Dashboard

```bash
streamlit run dashboard.py
```

Dashboard opens at:

```text
http://localhost:8501
```

---

## ☁ ThingSpeak Configuration

Create a ThingSpeak Channel.

Configure Fields:

| Field   | Data           |
| ------- | -------------- |
| Field 1 | Latitude       |
| Field 2 | Longitude      |
| Field 3 | Vehicle Status |
| Field 4 | Alert Type     |
| Field 5 | Speed          |

Update API Key:

```python
WRITE_API_KEY = "YOUR_WRITE_API_KEY"
```

Read API Key:

```python
READ_API_KEY = "YOUR_READ_API_KEY"
```

Channel ID:

```python
CHANNEL_ID = "YOUR_CHANNEL_ID"
```

---

## 📊 Dashboard Modules

### KPI Cards

* Latitude
* Longitude
* Speed
* Vehicle Status
* Alert Status

### Live Map

* Real-time vehicle position
* Google Maps integration

### Analytics

* Alert Statistics
* Status Statistics

### Vehicle History

* Historical location records
* Status logs

### Alert History

* Theft alerts
* Geofence alerts

---

## 🔐 Theft Prevention Workflow

```text
Vehicle Movement
        │
        ▼
Location Monitoring
        │
        ▼
Geofence Check
        │
 ┌──────┴──────┐
 │             │
Inside      Outside
 │             │
 ▼             ▼
Normal     Alert Generated
                │
                ▼
        Theft Detection
                │
                ▼
       Dashboard Notification
```

---

## 📸 Project Screenshots

### Dashboard Home

Add:

```text
images/dashboard_home.png
```

### Live Vehicle Tracking

Add:

```text
images/live_map.png
```

### Vehicle History

Add:

```text
images/history.png
```

---

## 📚 Applications

* Fleet Management
* Vehicle Security
* Logistics Tracking
* Asset Monitoring
* Smart Transportation
* Industrial Vehicle Monitoring

---

## 🔮 Future Enhancements

* ESP32 Hardware Integration
* GPS Module Integration
* GSM/SMS Alerts
* Mobile Application
* Firebase Integration
* Machine Learning-Based Theft Prediction
* Driver Behavior Analytics

---

## 👨‍💻 Author

### Vayunandan Mishra

B.Tech Student
Internet of Things (IoT) Enthusiast
Python Developer | Embedded Systems | Cloud IoT

GitHub:

https://github.com/Vayu-143

---

## 📜 License

This project is developed for educational, academic, and research purposes.

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

📢 Share with others

---

**Built with ❤️ using Python, Streamlit, ThingSpeak, and IoT Technologies**
