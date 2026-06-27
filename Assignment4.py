# Q1. Lambda function 
print('Q1')
print("Write a lambda function named square that takes a number x and returns its square. \nCall the lambda function with input from the user and print the result.")
print()
#lambda function
sqr = lambda x: x * x

num = int(input("Enter a number : "))
print("Square using lambda : ", sqr(num))

# normal function 
def sqr_fun(x):
    return x * x

print("Square using normal function : ", sqr_fun(num))

#comparison :
#Lambda function :
# - short and anonymous (no function name required).
#- used for simple one - line operations.

#normal def function :
#- has a functon name.
#-better for complex logic and multiple statements.
print('\n')

#Q2. Lambda with Multiple Arguments
print('Q2')
print("Create a lambda function add_three(a, b, c) that returns the sum of three numbers. Take three numbers as input from the user and print their sum using this lambda function.")
print()

add_three = lambda a, b, c : a + b + c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Sum =", add_three(a, b, c))

print()


#Q3. loop for revision
print('Q3')
print("Write a program using a for loop and range() to:\na) Print all numbers from 1 to 25.\nb) Print the sum of all numbers from 1 to 20.\nc) Print the table of 5 5 1 to 5 10.")
print()

# A for loop is used when we know how many times we want to repeat a task.
print(" a) Print all numbers from 1 to 25\n")
print("Numbers from 1 to 25:")
for i in range(1, 26):
    print(i)
print()

print("b) Print the sum of all numbers from 1 to 20\n")
sum = 0
for i in range(1, 21):
    sum += i
print("Sum of numbers from 1 to 20 =", sum)
print()

print("c) Print the table of 5 from 1 to 10\n")
print("Table of 5:")
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)
print()


#Q4.While Loop Revision
print('Q4')
print("While Loop Revision \nRepeatedly asks the user to enter a positive number. \nKeeps adding the numbers to a running total.\nStops when the user enters 0 or a negative number.\nFinally prints the total sum.")
print()

total = 0
while True:
    num = int(input("Enter a positive number: "))

    if num <= 0:
        break

    total += num

print("Total Sum =", total)
print()


#Q5. Math Module
print('Q5')
print("Write a program that imports the math module and does the following:\nTakes a number as input.\nPrints its square root using math.sqrt().\nPrints its factorial using math.factorial() (for positive integers only).\nPrints the ceiling and floor value using math.ceil() and math.floor().")
print()

import math
# The math module provides useful mathematical functions such as square root, factorial, ceiling, and floor.

no = float(input("Enter a number: "))

# Square Root
print("Square Root =", math.sqrt(no))

# Ceiling and Floor Values
print("Ceiling Value =", math.ceil(no))
print("Floor Value =", math.floor(no))

# Factorial (only for positive integers)
if no >= 0 and no.is_integer():
    print("Factorial =", math.factorial(int(no)))
else:
    print("Factorial can be calculated only for positive integers.")

print()


#Q6. Random Module
print('Q6')
print("Write a program using the random module that:\nGenerates and prints 5 random integers between 1 and 100.\nGenerates and prints one random number between 50 and 150.\nPrints a random floating point number between 0 and 1.\nUse different functions from the random module.")
print()

# Random Module Program

import random

# Generate and print 5 random integers between 1 and 100
print("5 Random Integers:")
for i in range(5):
    print(random.randint(1, 100))

# Generate and print one random number between 50 and 150
print("Random Number between 50 and 150:")
print(random.randint(50, 150))

# Generate and print a random floating-point number between 0 and 1
print("Random Floating Point Number:")
print(random.random()) 
print()

#Q7. Import Methods
print('Q7')
print("Demonstrate different ways of importing modules:\n1.Import the entire math module using import math and use math.pow(2, 4).\n2.Import only sqrt from math using from math import sqrt.\n3.Import math with an alias as m and use m.factorial(5).\nPrint the results with clear messages.")
print()

# Demonstrating Different Ways of Importing Modules

# 1. Import the entire math module
import math
print("2 raised to the power 4 =", math.pow(2, 4))

# 2. Import only sqrt from math
from math import sqrt
print("Square root of 25 =", sqrt(25))

# 3. Import math with an alias
import math as m
print("Factorial of 5 =", m.factorial(5))

print()


#Q8. Custom Module
print('Q8')
print("Create a custom module file named mymodule.py that contains:\nA function greet(name) that prints 'Hello [name], Welcome to Python Class!'\nA function calculate_power(base, exp) that returns base raised to exponent.\nThen write a main program that imports this module and uses both functions.")
print()

import forth

print(dir(forth))

name = input("Enter your name: ")
forth.greet(name)

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

result = forth.calculate_power(base, exp)

print("Power =", result)

print()

#Q9. name == "main"
print('Q9')
print("Creates a small function and demonstrates the use of if __name__ == "'__main__'": so that some code runs only when the file is executed directly")
print()

# Demonstration of if __name__ == "__main__"

def greet():
    print("Hello! Welcome to Python.")

# This block runs only when the file is executed directly
if __name__ == "__main__":
    print("Program is running directly.")
    greet()

print()


#Q10. Mini Project - Combined Concepts
print('Q.10')
print("Create a Simple Math Utility Program using functions, lambda, loops and modules:\n1.A lambda function to calculate square of a number.\n2.A normal function using math module to calculate power.\n3.Use a while loop to repeatedly ask the user for a number and choice Square / Power / Random Number).\n4.Use random module to generate a random number when chosen.")
print()

import math
import random

# Lambda function to calculate square
square = lambda x: x * x

# Normal function using math module to calculate power
def calculate_power(base, exp):
    return math.pow(base, exp)


# Main program using while loop
while True:
    print("\n===== Math Utility Menu =====")
    print("1. Square")
    print("2. Power")
    print("3. Random Number")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        num = float(input("Enter a number: "))
        print("Square =", square(num))

    elif choice == "2":
        base = float(input("Enter base: "))
        exp = float(input("Enter exponent: "))
        print("Power =", calculate_power(base, exp))

    elif choice == "3":
        print("Random Number =", random.randint(1, 100))

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please try again.")
