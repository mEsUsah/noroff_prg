import requests
from configparser import ConfigParser

# Get API key form .env file
config = ConfigParser()
config.read('.env')
API_KEY = config['API']['CAT']

def task():
    '''
    Visit The Cat API - Cats as a Service and try to create a Python API call to 
    request information regarding a specific cat breed.
    '''

    url = 'https://api.thecatapi.com/v1/breeds/abys'
    headers = {
        'x-api-key': API_KEY
    }

    response = requests.get(url, headers=headers)
    cat_info = response.json()
    for key, value in cat_info.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    task()
