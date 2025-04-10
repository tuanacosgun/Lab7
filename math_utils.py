def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero."

def power(x, y):
    return x ** y

def mod(x, y):
    return x % y

if __name__ == "__main__":
    print("Test cases for math_utils:")
    print("Add: ", add(5, 3))
    print("Subtract: ", subtract(10, 4))
    print("Multiply: ", multiply(6, 7))
    print("Divide: ", divide(8, 0))
    print("Power: ", power(2, 3))
    print("Mod: ", mod(10, 3))
