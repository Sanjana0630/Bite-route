import smtplib
import socket
from dotenv import load_dotenv
import os

load_dotenv()

def test_smtp():
    host = "smtp.gmail.com"
    port = 587
    user = os.getenv("EMAIL_HOST_USER")
    password = os.getenv("EMAIL_HOST_PASSWORD")

    print(f"--- SMTP Test for {host}:{port} ---")
    
    # 1. Test DNS resolution
    print(f"1. Testing DNS resolution for {host}...")
    try:
        ip = socket.gethostbyname(host)
        print(f"✅ Resolved {host} to {ip}")
    except socket.gaierror as e:
        print(f"❌ DNS Resolution failed: {e}")
        print("   This is why you see 'getaddrinfo failed'.")
        return

    # 2. Test Connection
    print(f"2. Connecting to {host}:{port}...")
    try:
        server = smtplib.SMTP(host, port, timeout=10)
        server.starttls()
        print("✅ Connection & TLS successful")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return

    # 3. Test Login
    if not user or user == "your-email@gmail.com":
        print("⚠️ Skipping login test: Credentials not set in .env")
        server.quit()
        return

    print(f"3. Attempting login for {user}...")
    try:
        server.login(user, password)
        print("✅ Login successful!")
    except Exception as e:
        print(f"❌ Login failed: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    test_smtp()
