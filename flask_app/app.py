# flask_app/app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    # !!! IMPORTANT: Replace this URL with your own!
    # Get it from Grafana: Dashboard -> Share -> Embed -> Copy the src="" part of the iframe.
    # Add "&kiosk" at the end for full-screen view.
    grafana_url = "http://localhost:3000/d/advxfjg/first-grafana-dashboard?orgId=1&kiosk"
    
    return render_template('dashboard.html', grafana_url=grafana_url)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)