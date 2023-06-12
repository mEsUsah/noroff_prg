class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        if self.__hours < 10:
            hours = "0" + str(self.__hours)
        else:
            hours = str(self.__hours)
        
        if self.__minutes < 10:
            minutes = "0" + str(self.__minutes)
        else:
            minutes = str(self.__minutes)
        
        if self.__seconds < 10:
            seconds = "0" + str(self.__seconds)
        else:
            seconds = str(self.__seconds)

        return f"{hours}:{minutes}:{seconds}"
    

    def __increase_sec(self):
        if self.__seconds == 59:
            self.__seconds = 0
            self.__increase_min()
        else:
            self.__seconds += 1


    def __increase_min(self):
        if self.__minutes == 59:
            self.__minutes = 0
            self.__increase_hour()
        else:
            self.__minutes += 1


    def __increase_hour(self):
        if self.__hours == 23:
            self.__hours = 0  
        else:
            self.__hours += 1


    def __decrease_sec(self):
        if self.__seconds == 0:
            self.__seconds = 59
            self.__decrease_min()
        else:
            self.__seconds -= 1


    def __decrease_min(self):
        if self.__minutes == 0:
            self.__minutes = 59
            self.__decrease_hour()
        else:
            self.__minutes -= 1

    
    def __decrease_hour(self):
        if self.__hours == 0:
            self.__hours = 23  
        else:
            self.__hours -= 1


    def next_second(self):
        self.__increase_sec()

    def prev_second(self):
        self.__decrease_sec()

if __name__ == '__main__':
    timer = Timer(23, 59, 59)
    print(timer)
    timer.next_second()
    print(timer)
    timer.prev_second()
    print(timer)
