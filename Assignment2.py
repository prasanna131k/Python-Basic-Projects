#Q1. if statement
print('Q1.\nyou are eligible to vote ?')
age = int(input("enter your age :"))
if(age>=18):
 print("you are eliible to vote")
print() 



#Q2. if-else statement
print('Q2.\n check even or odd number')
num = int(input("enter a number :"))
if(num % 2 ==0):
 print('even number')
else:
    print('odd number')
print()

#Q3. if-else statement
print('Q3.\n Grade on parsentage enter by user')
par = float(input("enter your parsentage :"))
if(par>=90):
 print("Grade A - Excellent")
else:
      if(par>=75):
       print("grade B - Good")
      else:
            if(par>=60):
             print("Grade C - Average") 
            else:
                  if(par>=40):
                    print("Grade D - Pass")
                  else:
                        if(par<40):
                         print("Faill")

 
#Q4. For loop with range
#range is a built-in function in Python that generates a sequence of numbers. It is commonly used in for loops to iterate over a specific range of values. The syntax for the range function is as follows:
print('Q4.\n write a program using for loop and range() to')

print("Numbers from 1 to 30 :")
for i in range(1,31):
    print(i)

print("Numbers from 1 to 50 (odd numbers only) :")
for i in range(1,51,2):
    print(i)

print("sum of numbers from 1 to 15 :")
total = 0
for i in range(1,16):
    total += i
print(total)
print()

#Q5. while loopis
print('Q5')
print("print number 1 to 20 and cube")
print("Numbers from 1 to 20 :")
x = 1
while x <= 20:
    print(x)
    x =x + 1

y = 1
while y <= 20:
    print(y ** 3)
    y = y + 1


#Q7. Nested if statement 
print('Q7. \n temperature and rain')
temp = int(input("Enter temperature : "))
is_rain = input("Is it raining ? (yes/no) :")

if(temp > 30):
    if(is_rain =="yes"):
        print("Hot and rainy, carry umbrela.")
    else:
        print("Hot day, wear light cloathes")
else:
    if(temp < 15):
        if(is_rain == "yes"):
            print("cold and rainy, wear jacket and take umbrela.")
        else:
            print("cold day, wear warm clothes.")
    else:
        print("Wearher is pleasent. Have a nice day!")




#Q8. for loop + if-elif-else
print('Q8.\n fizzbuss')
for i in range(1, 41):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)


#Q9. menu driven program
print('Q9. \n menu drive program...  simple calculator')
while True:
    print("Menu:")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print(f"The sum is: {result}")
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print(f"The difference is: {result}")
    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print(f"The product is: {result}")
    elif choice == '4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            result = num1 / num2
            print(f"The quotient is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


#Q10. Debugging
print('Q10.\n debugging')

num = int(input("Enter a number :"))  #num = input(...) error , 
if(num > 100):     # missing after coaln (:) , if(num>100)   error
    print("large number")
elif(num > 50):    #missing after colan
    print("medium number")
else:    # missing after caoln
    print("small number")
count = 1
while count <= 10 :  #missing after coaln
 print(count)
 count = count + 1


#Q6 while loop - user controller
print("Q6.\n repeatedly asks the uder enter a positiv number")
print("")
total = 0

while True :
    num = int(input("Enter a positive number : "))
    if num <= 0 :
     break
    total = total + num

print("total sum = ", total)


