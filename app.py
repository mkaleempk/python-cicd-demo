from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on EC2 via Jenkins!"

if __name__ == '__main__':
    # Important: host='0.0.0.0' makes it public
    app.run(host='0.0.0.0', port=5000)
