import math

def calculate_area_of_shape(shape: str, lenght=0, height=0, width=0, radius=0) -> float:
    """
    Calculate the area of a shape.
    
    rectangle: heigth, width
    square: length
    triangle: height, widht
    circle: radius

    Returns a float
    """

    if shape.lower() == "rectangle":
        return float(height * width)
    elif shape.lower() == "square":
        return float(lenght**2)
    elif shape.lower() == "triangle":
        return float((height * width) / 2)
    elif shape.lower() == "circle":
        return float(math.pi * radius**2)


if __name__ == "__main__":
    print(calculate_area_of_shape("square", lenght=20))
    print(calculate_area_of_shape("rectangle", height=20, width=30))
    print(calculate_area_of_shape("triangle", height=20, width=20))
    print(calculate_area_of_shape("circle", radius=10))
    