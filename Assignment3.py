#Q1. Basic function()
print('Q1')
print('Write a function named welcome()  \n Ans :-')
print()
#Function are useful because they help us reuse code 
#make program easier to read, and avoid repetition.

def welcome():
 print("Welcome to Python programming!")

welcome()

print('\n')



#Q2.Function with parameters 
print('Q2')
print('Create a function named greet(name) that parameter name and print:')
print()

def greet(name):
    print("Hello", name +" " "Welcome back.")

greet("prasanna!")
greet("sakura!")

print('\n')


#Q3. Default parameter
print('Q3')
print('Write a function show_message(message="Hello) that prints the message')
print()
#Default parameters are useful because they provide a default value
#when no argument is passed , making the function more flexible .
def show_message(message="hello"):
    print(message)

show_message()
show_message("welcome to python")


print('\n')


#Q4. Function with multipale parameters & return
print('Q4')
print('Creat a function calculate_sum(a,b) that takes two numbers and returns their sum')

#Function that returns the sum of two numbers
def sum(a,b):
    return a+b

#calling the function and storing the result
result = sum(2,2)
print(result)

#demonstrating print() inside a function 
def sum_print(c, d):
    print('sum =',c+d)

sum_print(3,3)

#return sends the value back to the place where the function was called, so it can be stored in a variable and used later.

#print() only display the value on the screen.


print('\n')


#Q5. positional vs keyword arguments
print('Q5')
print('write a function student_info(name, age) that prints the name and age. call this function twice.')

def std_info(name,age):
    print("name :", name)
    print("age :", age)

#1. Using positional argument 
#value are assigned based on their position.
std_info("prasanna",18)
print() # Blank line for readability.

#2. Using keyword argument 
#Values are assigned using parameter names,
#so the order does not matter.
std_info(age=19 , name="sakura")
print()

#6. Function with return value.
print('Q6')
print('Write a function square(num) that returns the square of the given number.\n Write another function cube(num) that returns the cube of the number. In the main program,\n take a number as input from the user and print its square and cube using these functions.\n')

def sqr(num):
    return num * num
def cube(num):
    return num * num * num

number = int(input("Enter a number : "))
print("squre :", sqr(number))
print("Cube :", cube(number))
print()


#Q7. Recursion - Basic
print('Q7')
print('Write a recursive function countdown(n) that prints numbers from n down to 1. \nCall countdown(10). Make sure to include the base case (stopping condition)\n')

def count(n):
    if(n==0):
        return
    print(n)
    count(n-1)

count(10)
print()


#Q8. Recursion - Factorial
print('Q8')
print("Write a recursive function factorial(n) that calculates and returns the factorial of a number.")

def factorial(n):
    #Base case : factorial of 0 or 1 is 1 
    if (n==0 or n==1):
        return 1
    return n + factorial(n - 1)

num = int(input("Enter a number : "))

print("Factorial = ", factorial(num))
print()


#Q9.Scope - local vs global
print('Q9')
print('Write a program to demonstrate scope :')



total = 0
#Function to add a value to the global variable
def add_val(x):
    global total
    total = total + 1
    print("Total : ", total)

add_val(10)
add_val(20)
add_val(30)

#Function with a local variable
#def demo_local():
 #   loacal_var = "I am a local variable"
  #  print(local_var)

#demo_local()

#Trying to access a local variable outside its function 
#this will cause an error:
#print(local_val)
print()


#Q10.mini progect - all concept
print('Q10')
print('Create a simple number analyzer program using functions :')

def get_num():
    return int(input("Enter a Number (0 to exit) : "))

def is_even(num):
    return num % 2 == 0

def power(base, exp=2):
    return base ** exp

def show_result(num):
    if (is_even(num)):
        print(num, "is Even")
    else:
        print(num, "is Odd")

    print("Squre = ", power(num))
    print()

while True:
    number = get_num()

    if(number == 0):
        print("Program Ended!")
        break

    show_result(num)



    
