def print_alternatives(alternatives):
    for index, alternative in enumerate(alternatives):
        print(f"{index}: {alternative['name']} - {alternative['price']},- ")


def verify_user_input(user_input, alternatives):
    if user_input.isnumeric() and int(user_input) in range(len(alternatives)):
        return True
    else:
        return False
    

def select_alternative(alternatives, text):
    while True:
        print_alternatives(alternatives)
        
        user_answer = input(f"{text}: ")
        if verify_user_input(user_answer, alternatives):
            print() # Empty line
            return int(user_answer)
        else:
            print("Not a valid choice, try agian. \n")


def print_summmary(total_price):
    print("-"*80)
    print(f"Total amount to pay: {total_price}")


base_alternatives = [
    {
        "name": "Thick",
        'price': 10
    },{
        "name": "Thin",
        'price': 5
    }
]
size_alternatives = [
    {
        "name": "Small",
        'price': 30
    },{
        "name": "Medium",
        'price': 40
    },{
        "name": "Large",
        'price': 50
    }
]
sause_alternatives = [
    {
        "name": "Tomato",
        'price': 5
    },{
        "name": "Barbicue",
        'price': 10
    }
]
topping_alternatives = [
    {
        "name": "Cheese",
        'price': 5
    },{
        "name": "Mushrooms",
        'price': 3
    },{
        "name": "Avocado",
        'price': 7
    },{
        "name": "Pineapple",
        'price': 5
    },{
        "name": "Chicken",
        'price': 7
    },{
        "name": "Fish",
        'price': 6
    }
]

def task() -> None:
    """
    A pizza shop owner has asked you to write a script that allows a customer 
    to calculate the cost of a pizza. 
    
    He has asked you to make the following options available to the customer:

    - Pizza base (Customer must choose 1): 
        - Thick (Kr 10) or Thin (Kr 5).
    - Pizza size (Customer must choose 1): 
        - Small (Kr 30), Medium (Kr 40), or Large (Kr 50).
    - Basic sauce (Customer must choose 1): 
        - Tomato (Kr 5) or Barbecue (Kr 10).
    - Toppings (Customer may choose any or none): 
        - Cheese (Kr 5), Mushrooms (Kr 3), Avocado (Kr 7), Pineapple (Kr 5), Bacon (Kr 7), Chicken (Kr 7) or Fish (Kr 6).
    """
    total_price = 0

    selected_base = select_alternative(base_alternatives, "Select base")
    total_price += base_alternatives[selected_base]['price']

    selected_size = select_alternative(size_alternatives, "Select size")
    total_price += size_alternatives[selected_size]['price']

    selected_sause = select_alternative(sause_alternatives, "Select sause")
    total_price += sause_alternatives[selected_sause]['price']

    selected_toppings = select_alternative(topping_alternatives, "Select topping")
    total_price += topping_alternatives[selected_toppings]['price']

    print_summmary(total_price)

if __name__ == "__main__":
    task()
