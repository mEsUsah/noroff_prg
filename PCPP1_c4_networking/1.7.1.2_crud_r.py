import requests

try:
    reply = requests.get("http://localhost:3000/cars")
except requests.RequestException:
    print("Communication error")
else:
    print(reply.headers['Content-Type'])
    if reply.status_code == requests.codes.ok:
        print(reply.text)
    else:
        print("Server error")