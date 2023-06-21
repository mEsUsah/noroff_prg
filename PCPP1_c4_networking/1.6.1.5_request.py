import requests

reply = requests.get("http://localhost:3000/cars")
if reply.status_code == requests.codes.ok:
    print(reply.headers['content-type'])
    print(reply.text)

