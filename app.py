# app.py
import datetime
import socket

def main():
    print("=" * 50)
    print("🚀 Simple Python App Deployed via Jenkins")
    print("=" * 50)
    print(f"🕒 Time now: {datetime.datetime.now()}")
    print(f"💻 Hostname: {socket.gethostname()}")
    print("✅ Jenkins CI/CD test successful!")
    print("=" * 50)

if __name__ == "__main__":
    main()
