def worked_hours(total_minutes: int) -> str:
    """
    A manager has requested that you write a script that allows him to enter a value 
    representing the number of minutes one of his employees has worked in a month. 
    
    He wants the script to use the number of minutes to calculate 
    the number of days worked in the month, 
    the number of hours left over (not adding up to a full working day) and 
    the number of minutes left over (not adding up to a full hour). 
    
    For the sake of this calculation, a working day consists of eight hours. 
    Once calculated, display the resulting calculation in the following format: 
    
    working days:hours:minutes.
    """
    day = 60*8
    
    days = total_minutes // day
    leftover_minutes = total_minutes % day

    hours = leftover_minutes // 60
    minutes = leftover_minutes % 60
    
    return f"{days}:{hours}:{minutes}"


if __name__ == "__main__":
    print(worked_hours(60*7))