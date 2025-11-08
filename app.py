# app.py
from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <html>
    <head><title>Jenkins Python CI/CD Demo</title></head>
    <body style='text-align:center;font-family:sans-serif;'>
        <h1 style='color:green;'>🚀 Python Web App via Jenkins CI/CD</h1>
        <p>✅ Deployment successful!</p>
        <p>🕒 Time now: {datetime.datetime.now()}</p>
        <p>💻 Hostname: {socket.gethostname()}</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
