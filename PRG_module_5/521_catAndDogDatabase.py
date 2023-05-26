import requests
import os
from configparser import ConfigParser

# Static variables
DISPLAY_DETAILS = 0
SHOW_IMAGE = 1
DOGS = 0
CATS = 1


# Get API key form .env file
config = ConfigParser()
config.read('.env')
API_KEY = config['API']['CAT']

def open_webpage(url):
    print('Opening the URL in Chrome...')
    os.system(f"start chrome {url}")


def print_info(data):
    print('*' * 80)
    print(f"Name: {data['name']}")
    print(f"Origin: {data['origin']}")
    print('*' * 80)


def menu(options):  
    for i, option in enumerate(options):
        print(f'{i + 1}: {option}')

    while True:
        try:
            selected = int(input('Select a number: '))
        except:
            print('Error, invalid selection. ', end="")
            continue
        
        if selected > 0 and selected <= len(options):
            selected -= 1
            break

    return selected


def handle_options(main_menu_selected, second_menu_selected):
    if main_menu_selected == DOGS:
        if second_menu_selected == DISPLAY_DETAILS:
            get_dog_info()
        if second_menu_selected == SHOW_IMAGE:
            get_dog_image()
    elif main_menu_selected == CATS:
        if second_menu_selected == DISPLAY_DETAILS:
            get_cat_info()
        if second_menu_selected == SHOW_IMAGE:
            get_cat_image()


def get_dog_info():
    url = 'https://api.thedogapi.com/v1/breeds/2'
    headers = {
        'x-api-key': API_KEY
    }

    try:
        response = requests.get(url, headers=headers)
        dog_info = response.json()
        print_info(dog_info)
    except:
        print('Whoops, something went wrong with the API call')


def get_dog_image():
    url = 'https://api.thedogapi.com/v1/images/search'
    headers = {
        'x-api-key': API_KEY
    }

    try:
        response = requests.get(url, headers=headers)
        dog_info = response.json()[0]
        
        image_url = dog_info['url']
        open_webpage(image_url)
    except:
        print('Whoops, something went wrong with the API call')


def get_cat_info():
    url = 'https://api.thecatapi.com/v1/breeds/abys'
    headers = {
        'x-api-key': API_KEY
    }

    try:
        response = requests.get(url, headers=headers)
        cat_info = response.json()
        print_info(cat_info)
    except:
        print('Whoops, something went wrong with the API call')


def get_cat_image():
    url = 'https://api.thecatapi.com/v1/images/search'
    headers = {
        'x-api-key': API_KEY
    }

    try:
        response = requests.get(url, headers=headers)
        cat_info = response.json()[0]
        
        image_url = cat_info['url']
        open_webpage(image_url)
    except:
        print('Whoops, something went wrong with the API call')
    

if __name__ == '__main__':
    main_menu_options = ('Dogs','Cats','Exit program')
    second_menu_options = ('Display details','Show image','Return to main menu')
    
    while True:
        # Show main menu
        main_menu_selected = menu(main_menu_options)
        
        # Quit program if selected
        if main_menu_selected == len(main_menu_options) - 1:
            exit()

        # Show second menu
        second_menu_selected = menu(second_menu_options)

        # Return to main menu if selected
        if second_menu_selected == len(second_menu_options) - 1:
            continue
        
        # Perform actions based on user selections
        handle_options(main_menu_selected, second_menu_selected)
