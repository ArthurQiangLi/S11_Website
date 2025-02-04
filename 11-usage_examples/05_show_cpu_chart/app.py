from flask import Flask, render_template, jsonify
import psutil
import time
import threading
from collections import deque

app = Flask(__name__)

cpu_list = deque(maxlen=30)# Store the last 30 CPU data points, used as FIFO (collected every 0.5s)
memory_list = deque(maxlen=30)

## note, if you want 'cpu' and 'memory' are display in a combined chart, they should have the same data rate.
def collect_data():
    memory_update_counter = 0  # Track when to update memory
    while True:
        timestamp = time.strftime("%H:%M:%S")  # Generate timestamp
        cpu_usage = psutil.cpu_percent(interval=0.5) # Store CPU usage (2Hz)
        cpu_list.append({"time": timestamp, "cpu": cpu_usage})
        memory_usage = psutil.virtual_memory().percent 
        memory_list.append({"time": timestamp, "memory": memory_usage})
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify(cpu=list(cpu_list), memory=list(memory_list))


if __name__ == '__main__':    
    threading.Thread(target=collect_data, daemon=True).start()# Start background thread to collect data
    app.run(debug=True, host='0.0.0.0', port=5000)

