# 1. Default Argument Function
# 2. Keyword Argument Function
# 3. Arbitrary Argument Function
# 4. Keyword Arbitrary Argument Function

def printData(name="USER",city="SOLAPUR"):
    print(f"My name is {name}. I live in {city}.")

def add(a,b=0):
    result = a+b
    print(result)

add(10,20)
printData("aayesh","pune")
printData()