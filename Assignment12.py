#Q2. Strings + Loops + Functions
print("Q1")
print()

def analyze_string(s):
    print("Length of string :- ", len(s))

    print("Reversed string :- ", s[::1])

    vowels = "aeiou"
    count = 0
    for ch in vowels:
        count += 1
    print("Number of vowels :- ", count)

    print("\nCharactor with Positive and Negative Index :- ")
    for i in range(len(s)):
        print(f"Character :-  {s[i]} Positive index :- {i} Negative index :- {[i - len(s)]}")


text = input("Enter a String :- ")
if text == "" :
    print("Empty String Entered.")
else :
    analyze_string(text)


print("------------------------------------------------------------------------------------------------")


print("\n")
#Q3. Lists + Functions + Exception Handling 
print("Q3")
print()

def  manage_marks():
    marks = []

    for i in range(5):
        while True:
            try :
                mark = float(input(f"Enter marks of subject {i + 1}: "))
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input! Please enter Numeric marks only. ")

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    marks.sort(reverse=True)

    print("\nAverage Marks :- ", average)
    print("Highest Marks :- ", highest)
    print("Lowest marks :- ", lowest)
    print("Marks of Descenfing Order :- ", marks) 


manage_marks()


print("-----------------------------------------------------------------------------------------------")


print("\n")
#Q4. OOP  Lists + Exception Handling
print("Q4")
print()



class Student:

    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    
    def add_mark(self, mark):
        try:
            mark = float(mark)

            if mark < 0 or mark > 100:
                raise ValueError

            self.marks_list.append(mark)
            print("Mark added successfully.")

        except ValueError:
            print("Invalid marks! Enter marks between 0 and 100.")

    
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

    
    def display_info(self):
        print("\n----- Student Details -----")
        print("Name :", self.name)
        print("Roll No :", self.roll_no)
        print("Marks :", self.marks_list)
        print("Average :", self.get_average())



name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

student = Student(name, roll_no)


for i in range(5):
    mark = input(f"Enter mark {i + 1}: ")
    student.add_mark(mark)


student.display_info()


print("---------------------------------------------------------------------------------------------")


print("\n")
#Q5. Dictionaries + Functions + Control Structures
print("Q5")
print()



def student_database():

    
    students = {}

    while True:
        print("\n----- Student Database Menu -----")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                roll_no = int(input("Enter Roll Number: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                
                students.update({
                    roll_no: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })

                print("Student added successfully.")

            except ValueError:
                print("Invalid input! Please enter correct values.")

        elif choice == "2":
            try:
                roll_no = int(input("Enter Roll Number to Search: "))

                
                student = students.get(roll_no)

                if student:
                    print("\nStudent Details")
                    print("Name :", student["Name"])
                    print("Age :", student["Age"])
                    print("City :", student["City"])
                else:
                    print("Student not found.")

            except ValueError:
                print("Invalid Roll Number.")

        elif choice == "3":
            if len(students) == 0:
                print("No student records available.")
            else:
                print("\nAll Student Records")
                for roll_no, details in students.items():
                    print("\nRoll No:", roll_no)
                    print("Name :", details["Name"])
                    print("Age :", details["Age"])
                    print("City :", details["City"])

        elif choice == "4":
            print("Exiting Program...")
            break

        else:
            print("Invalid choice! Please try again.")



student_database()



print("-------------------------------------------------------------------------------------------------")


print("\n")
#Q6. Sets + Tuples + Modules
print("Q6")
print()



import random
import math


numbers = set()


try:
    for i in range(10):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.add(num)

    
    num_tuple = tuple(numbers)

    print("\nUnique Numbers (Set):", numbers)
    print("Tuple:", num_tuple)

    
    if len(num_tuple) >= 3:
        random_numbers = random.sample(num_tuple, 3)
        print("3 Random Numbers:", random_numbers)
    else:
        print("Not enough unique numbers to pick 3 random numbers.")

    
    total = sum(num_tuple)

    if total >= 0:
        print("Square Root of Sum:", math.sqrt(total))
    else:
        print("Cannot find square root of a negative number.")


except ValueError:
    print("Invalid input! Please enter only numbers.")


print("------------------------------------------------------------------------------------")


print("\n")
#Q7. Lambda + range() + Lists + Exception Handling
print("Qq7")
print()


square = lambda x: x * x

try:
    
    squares = []

    
    for i in range(1, 21):
        squares.append(square(i))

    print("Squares:", squares)

    print("\nEven Squares:")
    for num in squares:
        if num % 2 == 0:
            print(num)

except Exception as e:
    print("Error:", e)


print("--------------------------------------------------------------------------------------------")


print("\n")
#Q8. Tuples + Dictionaries + OOP
print("Q8")
print()



class Employee:

    
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (department, salary)
    

    
    def show_details(self):
        print("Employee ID :", self.emp_id)
        print("Name :", self.name)
        print("Department :", self.details[0])
        print("Salary :", self.details[1])
        print()



employees = {}


for i in range(3):
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    emp = Employee(emp_id, name, department, salary)

    
    employees[emp_id] = emp


print("\nEmployee Details")
for emp in employees.values():
    emp.show_details()



print("-----------------------------------------------------------------------------------------------")


print("\n")
#Q9. Strings + Sets + Exception Handling + Modules
print("Q9")
print()



import math

try:
    
    sentence = input("Enter a sentence: ")

    
    words = set(sentence.split())

    
    print("Unique Words:")
    for word in sorted(words):
        print(word)

    
    count = len(words)


    print("Unique Words Count^2:", math.pow(count, 2))

except Exception:
    print("An error occurred.")



print("----------------------------------------------------------------------------------------")


print("\n")
#Q10.  Mini Project - Comprehensive
print("Q10")
print("mini Project!")
print()



import math
import random


history = {}


def arithmetic():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter your choice: ")

        if choice == "1":
            result = a + b
        elif choice == "2":
            result = a - b
        elif choice == "3":
            result = a * b
        elif choice == "4":
            result = a / b
        else:
            print("Invalid Choice")
            return

        print("Result:", result)

        key = input("Enter timestamp (Example: 10:30 AM): ")
        history[key] = result

    except Exception:
        print("Invalid Input")


while True:

    print("\n----- Smart Calculator -----")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Generate Random Number")
    print("4. View History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        arithmetic()

    elif choice == "2":
        num = float(input("Enter a number: "))
        print("Square Root:", math.sqrt(num))

    elif choice == "3":
        print("Random Number:", random.randint(1, 100))

    elif choice == "4":
        print("\nHistory")
        for key, value in history.items():
            print(key, ":", value)

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")




