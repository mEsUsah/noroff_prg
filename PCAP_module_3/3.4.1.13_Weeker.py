class WeekDayError(Exception):
    pass
	

class Weeker:
    weekdays = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

    def __init__(self, day):
        if day not in Weeker.weekdays:
            raise WeekDayError
        self.day = Weeker.weekdays.index(day)

    def __str__(self):
        return Weeker.weekdays[self.day]

    def add_days(self, n):
        self.day = n % 7 + self.day

    def subtract_days(self, n):
        modulo = (n % 7)
        if self.day - modulo < 0:
            rest = self.day - modulo
            self.day = 7 + rest
        else:
            self.day = self.day - modulo


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
