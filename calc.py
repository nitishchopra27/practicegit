#!/usr/bin/python3
# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return (x / y)

a = add(5 ,6)
print("Result of addition is: ", a)

b = subtract(6, 5)
print("Result of subtraction is: ", b)

c = multiply(5, 6)
print("Result of multiplication is: ", c)

d = divide(10, 5)
print("Result of division is: ", d)