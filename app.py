from flask import Flask, render_template_string, jsonify
import os
import time
from datetime import datetime
from get_save_time import retrieve_paris_legal_time

app = Flask(__name__)
FILE_PATH = "Observatoire_de_Paris.txt"

# Function to calculate time difference
def time_difference(last_modified_time):
    current_time = time.time()
    time_passed = current_time - last_modified_time
    hours = time_passed // 3600
    minutes = (time_passed % 3600) // 60
    seconds = int(time_passed) % 60
    milliseconds = int((time_passed - int(time_passed)) * 1000)
    return int(hours), int(minutes), int(seconds), milliseconds

# Function to get last modified time
def get_last_modified_time():
    try:
        with open(FILE_PATH, "r") as file:
            lines = file.readlines()
            last_line = lines[-1]
            if "Last Modified Time (Epoch)" in last_line:
                return float(last_line.split(":")[-1].strip())
    except Exception as e:
        print(f"Error reading file: {e}")
    return None

# API endpoint for updating the time file
@app.route('/update')
def update_time():
    retrieve_paris_legal_time()
    return jsonify({"message": "File updated."})

# API endpoint to get time data for AJAX
@app.route('/data')
def get_time_data():
    last_modified = get_last_modified_time()
    if last_modified:
        hours, minutes, seconds, ms = time_difference(last_modified)
        current_pc_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        actual_time_epoch = last_modified + (hours * 3600 + minutes * 60 + seconds) + (ms / 1000)
        calculated_time = datetime.fromtimestamp(actual_time_epoch).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        return jsonify({
            "file_updated": datetime.fromtimestamp(last_modified).strftime("%Y-%m-%d %H:%M:%S"),
            "current_pc_time": current_pc_time,
            "calculated_time": calculated_time
        })
    return jsonify({"error": "File not found or invalid"}), 404

# Home route with frontend
@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Paris Legal Time Monitor</title>
            <script>
                function updateData() {
                    fetch('/data')
                        .then(res => res.json())
                        .then(data => {
                            document.getElementById("file-time").textContent = data.file_updated;
                            document.getElementById("pc-time").textContent = data.current_pc_time;
                            document.getElementById("calculated-time").textContent = data.calculated_time;
                        });
                }

                function updateFile() {
                    fetch('/update')
                        .then(res => res.json())
                        .then(data => {
                            console.log(data.message);
                            updateData();  // immediately refresh time
                        });
                }

                // Update data every second
                setInterval(updateData, 1000);

                window.onload = updateData;
            </script>
        </head>
        <body style="font-family: sans-serif; padding: 2rem">
            <h1>📡 Paris Legal Time Monitor</h1>
            <button onclick="updateFile()">🔄 Update Time File</button>
            <hr>
            <p><strong>🧮 Observatoire de paris Time (from file):</strong> <span id="calculated-time">Loading...</span></p>
            <p><strong>🖥️ Current PC Time:</strong> <span id="pc-time">Loading...</span></p>
            <p><strong>📁 File Last Updated:</strong> <span id="file-time">Loading...</span></p>
            
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
