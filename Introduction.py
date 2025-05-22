# Unit-I Introduction: Introduction to Networking, TCP/IP, DNS, Internet and its Evolution, World Wide Web, Web 2.0, Web 3.0, network communication protocols (HTTP/HTTPS, SMTP, IMAP, POP, FTP), client-server architecture, web applications architecture, application and web servers, web clients

# web_technologies_unit1.py

import socket
import http.server
import socketserver
import smtplib
import imaplib
import poplib
from urllib.parse import urlparse
import requests

# 1. TCP/IP Communication (Basic Socket Example)
def tcp_ip_demo():
    host = '127.0.0.1'
    port = 65432

    # TCP Server
    def start_server():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            print("TCP Server listening...")
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                conn.sendall(b"Hello from Server")

    # TCP Client
    def start_client():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(b"Hello Server")
            data = s.recv(1024)
            print("Received:", data.decode())

    return start_server, start_client


# 2. DNS Lookup Example
def dns_lookup(domain='www.google.com'):
    ip = socket.gethostbyname(domain)
    print(f'DNS Lookup for {domain}: {ip}')


# 3. HTTP/HTTPS Requests
def http_https_demo():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    print("HTTPS Request to JSONPlaceholder API:\n", response.json())


# 4. SMTP - Send Email (Example, won’t work without valid credentials)
def smtp_demo():
    sender = "your_email@gmail.com"
    password = "your_password"
    receiver = "receiver_email@example.com"
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, "Subject: Test Mail\n\nThis is a test.")
            print("Email sent successfully!")
    except Exception as e:
        print("SMTP Error:", e)


# 5. IMAP & POP (Read Emails - Needs real credentials)
def imap_demo():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login("your_email@gmail.com", "your_password")
        mail.select("inbox")
        status, messages = mail.search(None, "ALL")
        print("IMAP Inbox Message IDs:", messages)
    except Exception as e:
        print("IMAP Error:", e)

def pop_demo():
    try:
        pop = poplib.POP3_SSL("pop.gmail.com")
        pop.user("your_email@gmail.com")
        pop.pass_("your_password")
        num_messages = len(pop.list()[1])
        print("POP Inbox has", num_messages, "emails.")
    except Exception as e:
        print("POP Error:", e)


# 6. Simple HTTP Server (Web Server)
def start_web_server(port=8080):
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving HTTP on port {port}...")
        httpd.serve_forever()


# 7. Client-Server Web App Demo (Using Flask)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "<h1>Hello, Web Technologies!</h1><p>This is Web 2.0 style!</p>"

@app.route('/api/data')
def api_data():
    return {"message": "Welcome to Web 3.0 API!"}


# Run All Demos
if __name__ == "__main__":
    print("=== Web Technologies Unit I Demo ===\n")
    
    dns_lookup()  # DNS
    http_https_demo()  # HTTP/HTTPS
    
    # Start TCP Server & Client
    server, client = tcp_ip_demo()
    import threading
    threading.Thread(target=server, daemon=True).start()
    import time; time.sleep(1)
    client()

    # Flask Web App
    print("\nStarting Flask App (Web Server)... Visit http://127.0.0.1:5000")
    app.run(debug=False)
