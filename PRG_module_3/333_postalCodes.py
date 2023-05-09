POSTAL_CODES = {
    10: "Oslo",
    1662: "Rolvsøy",
    6413: "Molde",
    6631: "Batnfjordsøra",
    9006: "Tromsø",
}


def check_postal_code(zip: int) -> str:
    """
    Create a data structure able to store 10 postal codes with their associated 
    residential areas. Prompt the user to enter a postal code. 
    
    If the postal code exists, output the residential area linked to the postal code.
    """
    
    if not zip.isnumeric():
        return False
    else:
        zip = int(zip)

    
    if zip in POSTAL_CODES:
        return POSTAL_CODES[zip]
    else:
        return False

        
if __name__ == "__main__":
    found_address = check_postal_code(input("Enter a zip-code: "))
    if found_address:
        print(found_address)
    else:
        print("Sorry, did not find that zip-code in the dictionary...")
