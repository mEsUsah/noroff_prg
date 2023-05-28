from argparse import ArgumentParser
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

parser = ArgumentParser()

parser.add_argument('-t','--text', 
                    help="Text to encrypt", 
                    required=True,
                    nargs=1)

parser.add_argument('-k','--key', 
                    help="Passphrase for dectyption", 
                    required=True,
                    nargs=1)


def encrypt(plaintext:str, password:str):
    plaintext = plaintext.encode()
    password = password.encode()
    salt = 'salt-makes-people-eat-more'.encode()
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
    

if __name__ == '__main__':
    args = parser.parse_args()
    ciphertext =  encrypt(args.text[0], args.key[0])
    print(ciphertext)


