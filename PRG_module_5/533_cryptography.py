from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

SALT = 'salt-makes-people-eat-more'

def encrypt(plaintext:str, password:str):
    plaintext = plaintext.encode()
    password = password.encode()
    salt = SALT.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    fernet = Fernet(key)

    ciphertext = fernet.encrypt(plaintext)
    return ciphertext.decode()


def encryption_prompt():
    while True:
        print()
        plaintext = input("Plaintext to encrypt: ")
        password = input("Password: ")
        try:
            ciphertext = encrypt(plaintext, password)
            break
        except:
            print('Sorry, something went wrong')

    print(f'Ciphertext: {ciphertext}')


def decrypt(ciphertext:str, password:str):
    password = password.encode()
    salt = SALT.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    fernet = Fernet(key)

    plaintext = fernet.decrypt(ciphertext)
    return plaintext.decode()


def decryption_prompt():
    while True:
        print()
        ciphertext = input("Ciphertext to decrypt: ")
        password = input("Password: ")
        try:
            plaintext = decrypt(ciphertext, password)
            break
        except InvalidToken:
            print('Sorry, invalid ciphertext or password')

    print(f'Plaintext: {plaintext}')


def menu(options):  
    print()
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


## Main Program
if __name__ == '__main__':
    main_menu_options = ('Decrypt','Encrypt','Exit program')
    
    while True:
        # Show main menu
        main_menu_selected = menu(main_menu_options)
        
        if main_menu_selected == 0:
            decryption_prompt()

        if main_menu_selected == 1:
            encryption_prompt()
        
        if main_menu_selected == 2:
            exit()
    
        
