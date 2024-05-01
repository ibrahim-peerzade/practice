# Function with No Parameter No Return value
# Function with Parameter But No return value
# Function with No Parameter But Return value
# Function with Parameter and Return Both

def addition():
    num1 = int(input("ENTER FIRST NUMBER -  "))
    num2 = int(input("ENTER SECOND NUMBER - "))
    result = num1 + num2
    print(result)

def subtraction(a, b):
    result = a - b
    print(result)

def multiplication():
    num1 = int(input("ENTER A NUMBER - "))
    num2 = int(input("ENTER A NUMBER - "))
    result = num1 * num2
    return result

def division(n,d):
    return n // d

# addition()
# subtraction(150, 100)

# x = multiplication()
# print(x)

# subtraction(50,x)

print(division(35,5))

subtraction(division(50,2),multiplication())

