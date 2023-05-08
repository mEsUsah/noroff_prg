def metric_converter(centimeter: int) -> None: 
    """Converts a value from one centimeter to inches"""
    inches = centimeter / 2.54
    inches_with_two_decimals = '{:.2f}'.format(inches)
    print(f"{centimeter} centimeters is {inches_with_two_decimals} inches.")


if __name__ == "__main__":
    metric_converter(10)

    