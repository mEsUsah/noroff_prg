try:
    print("5"/0)
except ArithmeticError:
    print("ArithmeticError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("Unknown error")