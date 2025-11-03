from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics
import math
import time
import random

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Static information for the homepage
metrics.info('app_info', 'Test application for generating load', version='1.0.0')

@app.route('/')
def index():
    """Homepage: Renders a simple UI to trigger load generation."""
    return render_template('index.html')

@app.route('/cpu')
def cpu_intensive_task():
    """Simulates a CPU-intensive task."""
    start_time = time.time()
    for i in range(20_000_000):
        _ = math.sqrt(float(i))
    duration = time.time() - start_time
    return f"CPU-intensive task completed in {duration:.2f} seconds."

@app.route('/memory')
def memory_intensive_task():
    """Simulates a memory-intensive task by allocating a large object."""
    mb_to_allocate = random.randint(50, 150)
    # This creates a large list of strings in memory
    _ = [' ' * 1024] * (mb_to_allocate * 1024)
    time.sleep(1) # Hold the memory for a short duration
    return f"Allocated and released approximately {mb_to_allocate}MB of memory."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)