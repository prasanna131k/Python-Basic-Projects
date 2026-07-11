#Q1. Basic Class and Object
print("Q1")
print("Create a class named Car with:")
print()

# making class
class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print("Brand :- ", self.brand)
        print("Model :- ", self.model)

# now creating objects
car1 = car("toyota", "corolla")
car2 = car("Rolls-Royce", "phantom V8")

# now calling method
car1.display_info()
print()
car2.display_info()


print("--------------------------------------------------------------------")
#Q2. Using init Constructor
print("Q2")
print("Write a class Book that takes title, author, and price as parameters in __init__.\nCreate a method show_details() to print all the book information.\nCreate at least two book objects and display their details.")
print()

class book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        print("Title :- ", self.title)
        print("Auther :- ", self.author)
        print("Price :- ", self.price)


book1 = book("One peice!", "Eiichiro Oda", 18000)
book2 = book("Drigon Ball Z", "Akira Toriyama", 2199)

book1.show_details()
print()
book2.show_details()

print("----------------------------------------------------------")
#Q3. Instance Methods and self
print("Q3")
print("Create a class BankAccount")
print()

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited :- ", amount)

    def withdraw(self, amount):
        if amount <= self.balance :
            self.balance -= amount
            print("Withdrown :- ", amount)
        else:
            print("Indufficient Balance! ")
    
    def show_balance(self):
        print("Current Balance :- ", self.balance)
    
account = BankAccount("prasanna131k", 6000)

account.show_balance()
account.deposit(2000)
account.show_balance()
account.withdraw(3000)
account.show_balance()
account.withdraw(6000)


print("-------------------------------------------------------------------------------")
#Q4. Method with Parameters
print("Q4")
print("Create a class Student with attributes name and marks.\nAdd a method calculate_grade() that returns 'Pass' if marks ≥ 40, otherwise 'Fail'. \nCreate 3 student objects, display their details, and print their grades.")
print()

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Failll...!"

student1 = student("Amit", 70)
student2 = student("Priya", 35)
student3 = student("Rahul", 50)

print("Name :- ", student1.name)
print("Marks :- ", student1.marks)
print("Grade :- ", student1.calculate_grade())

print()

print("Name :- ", student2.name)
print("Marks :- ", student2.marks)
print("Grade :- ", student2.calculate_grade())

print()

print("Name :- ", student3.name)
print("Marks :- ", student3.marks)
print("Grade :- ", student3.calculate_grade())




print("------------------------------------------------------------------------------------------")
#Q5. Multiple Methods
print("Q5")
print("Create a class Employee class")
print()

class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Name :- ", self.name)
        print("Salary :- ", self.salary)
    
    def give_raise(self, amount):
        self.salary += amount 
        print("New Salary :- ", self.salary)

    def yearly_bonus(self):
        return self.salary * 0.10

emp = employee("Prasanna131k", 500000)
emp.display_details()
emp.give_raise(5000)
print("Yearly Bonus :- ", emp.yearly_bonus())



print("-------------------------------------------------------------------------------------------")
#Q6.Real-world Object Modeling
print("Q6")
print("Create a class MobilePhone with attributes: brand, model, battery_percentage.")
print()

class MobilePhone :
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage
    
    def charge(self, percent):
        self.battery_percentage += percent
        if self.battery_percentage > 100:
            self.battery_percentage = 100
        print("Battery charge.")

    def  use_phone(self, minutes):
        battery_used = minutes // 10
        self.battery_percentage -= battery_used
        if self.battery_percentage < 0:
            self.battery_percentage = 0
        print("Phone used for ", minutes, "minutes.")

    def show_status(self):
        print("Brand :- ", self.brand)
        print("Model :- ", self.model)
        print("Battery :- ", self.battery_percentage,"%")

phone = MobilePhone("Red magic", "11s Pro", 40)
phone.show_status()
phone.use_phone(180)
phone.show_status()
phone.charge(4)
phone.show_status()



print("-------------------------------------------------------------------------------------------")
#Q7. Combining Concepts
print("Q7")
print("Create a class Rectangle with attributes length and width.")
print()

# Class Definition
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())


length = float(input("Enter Length: "))
width = float(input("Enter Width: "))
rect = Rectangle(length, width)
rect.display()


print("---------------------------------------------------------------------------------")
#Q8. Updating Attributes
print("Q8")
print("Create a class Player with attributes name, score, and level.")
print()


class Player:
    def __init__(self, name, score, level):
        self.name = name
        self.score = score
        self.level = level

    def increase_score(self, points):
        self.score += points

    def level_up(self):
        self.level += 1

    def show_progress(self):
        print("Name:", self.name)
        print("Score:", self.score)
        print("Level:", self.level)



player1 = Player("Amit", 100, 1)

player1.show_progress()

player1.increase_score(50)
player1.level_up()

player1.increase_score(100)
player1.level_up()

print("\nAfter Updates:")
player1.show_progress()



print("-----------------------------------------------------------------------------------------")
#Q9.Debugging OOP Code
print("Q9")
print("The following code has errors. Correct it and add proper comments explaining thefixes:")

#class Person:
#def __init__(name, age):
#name = name
#age = age
#def introduce():
#print("My name is" name "and I am" age "years old.")
#p1 = Person("Rahul", 25)
#p1.introduce()


# Corrected Code
class Person:
    # Added 'self' parameter in __init__
    def __init__(self, name, age):
        # Use self to store values in object attributes
        self.name = name
        self.age = age

    # Added 'self' parameter in method
    def introduce(self):
        # Corrected print statement and accessed attributes using self
        print("My name is", self.name, "and I am", self.age, "years old.")

# Creating an object
p1 = Person("Rahul", 25)

# Calling the method
p1.introduce()



print("------------------------------------------------------------------------------Session 10 (AIML) - Assignment Questions")
#Q10. Mini Project - Combined OOP
print("Q10")
print("Create a Simple Library Management System using OOP :")
print()


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"

    def issue_book(self):
        if self.status == "Available":
            self.status = "Issued"
            print("Book issued successfully!")
        else:
            print("Book is already issued.")

    def return_book(self):
        if self.status == "Issued":
            self.status = "Available"
            print("Book returned successfully!")
        else:
            print("Book is already available.")

    def show_info(self):
        print("Title :", self.title)
        print("Author:", self.author)
        print("Status:", self.status)
        print("-" * 30)



library = []

while True:
    print("\n===== Library Management System =====")
    print("1. Add New Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Show All Books")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        library.append(Book(title, author))
        print("Book added successfully!")

    elif choice == 2:
        title = input("Enter Book Title to Issue: ")
        found = False

        for book in library:
            if book.title.lower() == title.lower():
                book.issue_book()
                found = True
                break

        if not found:
            print("Book not found!")

    elif choice == 3:
        title = input("Enter Book Title to Return: ")
        found = False

        for book in library:
            if book.title.lower() == title.lower():
                book.return_book()
                found = True
                break

        if not found:
            print("Book not found!")

    elif choice == 4:
        if len(library) == 0:
            print("No books available in library.")
        else:
            print("\nLibrary Books:")
            for book in library:
                book.show_info()

    elif choice == 5:
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")




