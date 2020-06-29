def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


if __name__ == "__main__":
    oprnd = "+";
    a = 2
    b = 3
    if oprnd == "+":
        print(add(a, b))
    
    if oprnd == "-":
        print(subtract(a, b))
    if oprnd == "*":
        print(multiple(a, b))
