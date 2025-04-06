# Time Synchronization System for FrHack

This project is a **real-time time synchronization system** that integrates multiple time sources to ensure accurate timekeeping. It uses wireless technologies like **GNSS**, **PTP**, and **5G** to synchronize time, 
which is crucial for applications in systems like railways, where wired connections are not feasible.

The system fetches the time from the most accurate source available, smoothly transitions between sources when necessary, and displays the time on a **Flask-powered web interface**.

## Features
- **Real-Time Time Synchronization**: Continuously fetches time data from the backend and displays it on the web page.
- **Smooth Time Transition**: Ensures smooth updates when the source of time changes, preventing jitter.
- **Priority Source Selection**: The most accurate source (GNSS, PTP, 5G) is used to update the displayed time, and the source list is updated in real-time based on availability.
- **Web Interface**: Displays the current time, available sources, and their statuses on a user-friendly interface.

## Technologies Used
- **Python** (Flask) for the backend.
- **JavaScript** (Fetch API) for real-time updates and smooth transitions.
- **HTML/CSS** for the frontend interface.

## Requiirements
- Python 3
- ntplib for Python
- Flask
- datetime
- A web browser

## Usage
1) Run the "app.py" file.
2) Enter the url "http://127.0.0.1:5000" in your browser.
