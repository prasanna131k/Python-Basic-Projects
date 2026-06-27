print("Q1 (Variable & Naming Rules)")

#your_full_name 
print("your full name :-")
fullname = 'Prasanna B Manwar'
print(fullname)
#fullname variable is used to store name
print(type(fullname))
print()

#your_age 
print("your age :-")
age = 18
print(age)
#age variable is used to store age
print(type(age))
print()

#your heiht in meters 
print("your height in meters :-")
height = "***"
print(height)
#height variable is used to store height
print(type(height))
print()

#Wheather you are a student
print("are you a student? :-")
is_student = True #its your choise to filup (true / false)
print(is_student)
#is_student variable is used to store student status
print(type(is_student))



print("\n")
print("\nQ2 (Data Types)")
print()

print("Q2:- a & b")

str = "prasanna131k\n"
print(str, "is of type", type(str))
print()

int_val = 123
print('\n' "is of type", type(int))
print()

float_val = 123.00
print(float, "is of type", type(float))
print()

bool = True
print(bool, "is of type", type(bool))
print()

print("Q2:- c")

num1 = 123
float_num = float(num1)
print(float_num, "is of type", type(float_num))
#interger to float conversion , 
#float() is a built-in function in python which is used to convert a number or a string to a floating point number.
print()

num2 = 123.45
int_num = int(num2)
print(int_num, "is of type", type(int_num))
#float to interger conversion ,
#int() is a built-in function in python which is used to convert a number or a string to an integer.

print("\n")
print("\nQ3 (operators - Arithmetic)")
print()

a = 15
b = 4

print('Addition :-', a + b)
print('Subtraction :-', a - b)
print('Multiplication :-', a * b)
print('Modulus :-', a % b)
print('Exponentiation :-', a ** b)
print('Division :-', a / b)
print('Floor Division :-', a // b)
#division (/) operator returns the quotient of the division as a float, while floor division (//) operator returns the quotient as an integer by discarding the decimal part.

print("\n")
print("\nQ4 (comparison & logical operators)")
print()

x = 25
y = 30
z = 25

print("Is x greater than y? :-", x > y)

print("Is x equal to z? :-", x == z)

print("Is x less than or equal to y AND y is not equal to z? :-", x <= y and y != z)

print("Is x less than y OR y is equal to z? :-", x < y or y == z)



print ('\n')
print("\nQ5 (Input / Output)")
print()

#input user name and print it
name = input("Enter your name :- ")

#input user birth year and print it
birth_year = int(input("Enter your birth year :- "))

#calculate age from birth year and print it
current_year = 2026
age = current_year - birth_year

print('\n ------ User Details ------')
print("Name :-", name)
print("age :-", age ,"years")



print("\n")
print("\nQ7 (Comments) \n write a small program that calculates the area and perimeter of a rectangle:")
print()

#Using float() allows measurements with decimal values
length = float(input("Enter your length in meters :- "))

#width is also taken as float for more accurate BMI calculation
width = float(input("Enter your width in rectangle :- "))

#area helps to calculate BMI
area = length * width

#perimeter is also calculated for more comprehensive output
perimeter = 2 * (length + width)

print('\n ------ BMI Calculation Result ------')
print("Area of rectangle :-", area)
print("Perimeter of rectangle :-", perimeter)



print("\n")
print("\nQ8 (Operators - Assignment & Membership)")
print()

fruits = ['mango', 'apple', 'banana', 'cherry']
score = 50

#add 25 to score using += operator
score += 25

#check if 'apple' is in fruits list
is_apple_in_fruits = 'apple' in fruits

#check if 'grape' is not in fruits list
is_grape_not_in_fruits = 'grape' not in fruits  

print("Updated score after adding 25 :-", score)
print("Is 'apple' in fruits list? :-", is_apple_in_fruits)
print("Is 'grape' not in fruits list? :-", is_grape_not_in_fruits)


print("\n")
print("Q9 (mini project - all concepts)\n write a student profile  generator program that takes user input for name, age ,city and marks in 3 subjects\n calculates total marks and percentage ") 
print()

#input student information 
student_name = input("Enter student name :- ")
student_age = int(input("Enter student age :- "))
student_city = input("Enter student city :- ")

#marks in 3 subjects

print("\nEnter marks in 3 subjects :-")
subject1_marks = float(input("Subject 1 marks :- "))
subject2_marks = float(input("Subject 2 marks :- "))
subject3_marks = float(input("Subject 3 marks :- "))

#calculate total marks and percentage
total_marks = subject1_marks + subject2_marks + subject3_marks
percentage = (total_marks / 300) * 100

print('\n ------ Student Profile ------')
print("Name :-", student_name)
print("Age :-", student_age, "years")
print("City :-", student_city)
print("Total Marks :-", total_marks)
print("Percentage :-", percentage, "%")



print("\n")
print("\nQ10 (Debugging & Understanding)")
print()

stdName = "Alica"
stdAge = 20 #missing statement operator (=) to assign value to stdAge variable
stdCity = "Amsterdam" #string value missing quotes

print("My Name :-", stdName)
print("My Age :-", stdAge) #missing comma (,) to separate string and variable in print statement
print("My City :-", stdCity) #missing comma (,) 


#check if age is greater than 18 and print message adult
print("adult :", stdAge > 18)  #missing comma (,) before condition

