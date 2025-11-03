# flask_app/app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    # This URL embeds the Grafana dashboard.
    # The UID 'container-monitoring-dashboard' is defined in the grafana-dashboard.json file.
    # The '&kiosk' parameter provides a clean, full-screen view without Grafana's UI elements.
    grafana_url = "http://localhost:3000/d/container-monitoring-dashboard/container-host-monitoring-dashboard?orgId=1&refresh=10s&kiosk"
    
    return render_template('dashboard.html', grafana_url=grafana_url)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)