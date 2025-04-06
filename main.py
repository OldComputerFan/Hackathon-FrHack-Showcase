# This is the main Flask application that serves the web interface and handles time retrieval from different sources.
from flask import Flask, render_template, jsonify
import time
from datetime import datetime
from threading import Thread

# Importing the time retrieval functions from their respective modules
from galileo_time import get_galileo_time
from ptp_time import get_ptp_time
from network_time import get_network_time
from config import SIMULATE_GALILEO_FAILURE, SIMULATE_PTP_NOISE, SIMULATE_NETWORK_JITTER, TIME_PRIORITY, SIMULATE_GPS_FAILURE
from gps import get_gps_time

app = Flask(__name__)

# This will store the most accurate time and which source it came from
current_time = {"time": "", "source": "", "sources": {}}


def get_time_by_source(source):
    if source == "GALILEO":
        result = get_galileo_time()
        if SIMULATE_GALILEO_FAILURE or not result:  # GALILEO failure case
            return None
        return result, "GALILEO"
    
    elif source == "PTP":
        result = get_ptp_time()
        if SIMULATE_PTP_NOISE or not result:  # PTP failure case
            return None
        return result, "PTP"
    
    elif source == "5G":
        result = get_network_time()
        if SIMULATE_NETWORK_JITTER or not result:  # Network failure case
            return None
        return result, "5G"
    
    elif source == "GPS":
        result = get_gps_time()
        if SIMULATE_GPS_FAILURE or not result:
            return None
        return result, "GPS"

    
    return None

def select_best_time():
    sources = {}
    for source in TIME_PRIORITY:
        result = get_time_by_source(source)
        if result:
            sources[source] = {"status": "Available", "time": result[0]}
        else:
            sources[source] = {"status": "Not Available", "time": None}

    # Get the best time from the available sources
    for source in TIME_PRIORITY:
        if sources[source]["status"] == "Available":
            return sources[source]["time"], source, sources
        
    return datetime.utcnow(), "Fallback", sources

# Update time every second
def update_time():
    global current_time
    while True:
        best_time, source, sources = select_best_time()
        # Check if best_time is a datetime object and convert it to ISO format
        if isinstance(best_time, datetime):
            formatted_time = best_time.isoformat()
        else:
            formatted_time = best_time  # already a string, e.g. an error message

        current_time["time"] = formatted_time
        current_time["source"] = source
        current_time["sources"] = sources
        time.sleep(0.01)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_time')
def get_time():
    return jsonify(current_time)

if __name__ == '__main__':
    # Start the background thread to update the time
    time_thread = Thread(target=update_time)
    time_thread.daemon = True
    time_thread.start()

    app.run(debug=True)
