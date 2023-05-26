import requests
from configparser import ConfigParser

# Get API key form .env file
config = ConfigParser()
config.read('.env')
API_KEY = config['API']['DAD_JOKE']

def task():
    '''
    Scour the Internet for another free, public API, specifically one that requires 
    an API key. 
    
    Please register with the site to receive the key and read through 
    the API documentation. Then, demonstrate its use.
    '''

    url = 'https://dad-jokes.p.rapidapi.com/random/joke'
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com",
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    joke = response.json()['body'][0]
    
    print('*' * 80)
    print(joke['setup'])
    print(joke['punchline'], '😂')


if __name__ == '__main__':
    task()