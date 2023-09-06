# adding else statement
# this code checks if an individual is male or tall, from the boolean set in the variable
is_male = False
is_tall = True
if is_male and is_tall:
    print("You are a tall guy")
elif is_male and not(is_tall):
    print("You are a short man")
elif is_tall and not(is_male):
    print("You are a tall woman")
else:
    print("You are short woman")

# an basic arithmetic using functions
print("Perform an arithmetic, select your calculation below")
print("1: Addition")
print("2: Multiplication")
select = input("Select: ")

x = input("Enter number: ")
y = input("Enter another number: ")


# user defined function to perform addition 
def addition(a, b):
    return a + b
ans = addition(int(x), int(y))

# user defined function to perform multiplication
def multiplication(a, b):
    return a * b
mul = multiplication(int(x), int(y))

# run an if statement for thorough validation
if select == "1":
    print(ans)

elif select == "2":
    print(mul)
else:
    print("Fields cannot be empty")

# basic calculator where u need to input your operator
from math import *
x = input("Enter number: ")
op = input("Enter operator: ")
y = input("Enter another number")

if op == "+":
    print(int(x) + int(y))

elif op == "*":
    print(int(x) * int(y))

elif op == "-":
    print(int(x) - int(y))
elif op == "/":
    print(int(x) / int(y))

# or can basically set the input to float
x = float(input("Enter number: "))
op = input("Enter operator: ")
y = float(input("Enter another number: "))

if op == "+":
    print(ceil(x + y))
elif op == "-":
    print(ceil(x - y))
elif op == "*":
    print(ceil(x * y))
elif op == "/":
    print(ceil(x / y))
    

