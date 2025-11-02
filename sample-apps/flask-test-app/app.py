from flask import Flask, request
import math
import time

app = Flask(__name__)

@app.route('/')
def index():
    """Homepage: Shows a welcome message and instructions."""
    return """
    <h1>Test Application for Monitoring</h1>
    <p>Use the following endpoints to generate load:</p>
    <ul>
        <li><a href="/cpu-work" target="_blank">/cpu-work</a> - Runs a CPU-intensive task.</li>
        <li><a href="/memory-work" target="_blank">/memory-work</a> - Allocates 100MB of memory temporarily.</li>
    </ul>
    """

@app.route('/cpu-work')
def cpu_work():
    """
    Simulates a CPU-intensive task by performing millions of calculations.
    """
    start_time = time.time()
    print("Starting CPU-intensive task...")
    
    for i in range(50_000_000):
        _ = math.sqrt(i)
        
    end_time = time.time()
    duration = end_time - start_time
    print(f"CPU task finished in {duration:.2f} seconds.")
    return f"CPU-intensive task completed in {duration:.2f} seconds."

@app.route('/memory-work')
def memory_work():
    """
    Simulates a memory-intensive task by allocating a large string in memory.
    """
    start_time = time.time()
    mb_to_allocate = 100
    print(f"Allocating {mb_to_allocate}MB of memory...")
    
    large_string = ' ' * (mb_to_allocate * 1024 * 1024)
    
    time.sleep(2)
    
    end_time = time.time()
    duration = end_time - start_time
    print(f"Allocated and released memory in {duration:.2f} seconds.")
    return f"Allocated and released {mb_to_allocate}MB of memory in {duration:.2f} seconds."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)