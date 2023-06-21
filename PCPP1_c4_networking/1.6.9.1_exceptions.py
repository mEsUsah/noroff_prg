import requests

try:
    # reply = requests.get('http://localhost:3000/cars', timeout=0.001) # 1ms
    # reply = requests.get('http://localhost:3001/cars') # invalid port
    reply = requests.get('http://..') # invalid URL
except requests.exceptions.Timeout:
    print('Sorry, Mr. Impatient, you didn\'t get your data')
except requests.exceptions.ConnectionError:
    print('Nobody\'s home, sorry!')
except requests.exceptions.InvalidURL:
    print('Recipient unknown!')
else:
    print('Here is your data, my Master!')