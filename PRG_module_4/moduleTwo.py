from datetime import datetime
import time
import random

def create_time():
    '''
    This function should create a time object and return it.
    '''
    datetime_object = datetime.now()
    return datetime_object


def output_local_time(timeObject):
    '''
    This function should receive a time object as a parameter and display 
    the local_time associated with it.
    '''
    print(timeObject.strftime("%H:%M:%S"))


def calculate_difference(time_one, time_two):
    '''
    This function should receive two objects, subtract them from each other 
    and return the difference.
    '''
    return time_two - time_one


def generate_random(min, max):
    '''
    This function receives a maximum number as a parameter and then returns a 
    random number between 0 and the maximum number.
    '''
    return random.randint(min, max)


if __name__ == "__main__":
    # Testing procedure
    time_object_one = create_time()
    output_local_time(time_object_one)
    
    time.sleep(2)
    time_object_two = create_time()
    
    difference = calculate_difference(time_object_one, time_object_two)
    print(difference)

    print(generate_random(1,10))
