#Q1. Creating Dictionarie
print("Write a program to create dictionaries using different methods:")
print()

print("a) An empty dictionary using two different ways.")

print("i) USing curly bracs")
d = {}

print(d)
print(type(d))

print("ii) Using dict() constructor")
d2 = dict()

print(d2)
print(type(d2))

print()
print("b) A dictionary with string keys (name, city, course).")

d3 = {
    "name" : "exampal",
    "city" : "tokyo",
    "course" : "computer engineer"
}

print(d3)
print(type(d3))

print()
print("c) A dictionary with integer keys.")

d4 = {
    1 : "one",      # keys are integers
    2 : "two",
    3 : "three"
}

print(d4)
print(type(d4))

print()
print("d) A mixed data type dictionary (string, int, float).")

d5 = {
    "string" : "name",  #sring value
    "int" : 10,         #int value
    "float" : 5.5       #float value
}

print(d5)

print()



#Q2. Accessing and Modifying Elements
print("Q2")
print("Create the dictionary:")
print()

student = {
    "name" : "prasanna131k",
    "age" : 18,
    "city" : "AKOLA city",
    "marks" : 67.86
}

print(student)

print()
print("i) Print the value of 'name' using square brackets.\n")

print( "Printing name using square brackets :- ", student["name"])

print()
print("ii) Update the 'marks' to 92.")

student.update([("marks" , 92)])
print(student)

print()
print("iii) Add a new key 'grade' with value 'A'.")

student.update([('grade', 'a')])
print(student)

print()

#Q3. get(), keys(), values(), items()
print("Q3")
print("Create a dictionary:")
print()

person = {"name": "Priya", "age": 21, "profession": "Engineer"}
print("dictionary :- ", person)

print()
print("a) Using get() to access 'age' and a non-existing key 'salary' (with default value).")

print("age :- ", person.get("age"))
print("salary :- ",person.get("salary", "not available"))

print()
print("b) Print all keys using keys().")

print("key and pair :- ", person.keys())

print()
print("c) Print all values using values().")

print("all vlaues are :- ", person.values())

print()
print("d) Print all key-value pairs using items().")

print("all key-value pairs :- ", person.items())

print()

#Q4. Nested Dictionary
print("Q4")
print("Create a nested dictionary to store information of two students:")
print()

students = {
"s1": {"name": "Rahul", "age": 20, "marks": 88},
"s2": {"name": "Sneha", "age": 21, "marks": 95}
}

print(students)
print(students.items())
print(students["s2"]["marks"])
students["s1"]["math"] = 90
print(students)

print()
#Q5. update() and pop()
print("Q5")
print("Create a dictionary")
info = {"brand": "Samsung", "model": "A52", "price": 25000}
print(info)

print("Update it with new information: {'color': 'Black', 'price': 24000}")
info.update({"color": "Black", "price": 24000})

print("Remove the key 'model' using pop() and print the removed value.")
info.pop("model")
print(info)

print()
#Q6. popitem() and clear()
print("Q6")
print("Create a dictionary with at least 5 key-value pairs.")
print()

student1 = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA",
    "city": "Pune",
    "marks": 88
}

print(student1)

removed_item1 = student1.popitem()
print("\nFirst Removed IStem:", removed_item1)
print(student1)

student1.clear()

print("clear student data :- ",student1)

# Difference between pop() and popitem()

# pop(key):
# Removes a specific key and returns its value.
# Example: student.pop("age")

# popitem():
# Removes and returns the last inserted key-value pair
# in the form of a tuple (key, value).



print()
#Q7. copy() and setdefault()
print("Q7")
print("Create a dictionary:")
print()

d = {"a": 1, "b": 2}
print(d)

copying = d.copy()

d.setdefault("c", 3)
d.setdefault("a", 10)

print("original :- ", d)
print("coped :- ", copying)

print()

#Q8. fromkeys() and Membership
print("Q8")
print("Write a program that:\nUses dict.fromkeys() to create a dictionary with keys ['name', 'age', 'city']\nand default value None.\nTakes user input to fill these keys.\nChecks if a given key exists using in operator.")
print()

keys = ["name", "age", "city"]
person = dict.fromkeys(keys, None)

print("Initial Dictionary : - ", person)

person["name"] = input("Enter your name :- ")
person["age"] = input("Enter your age :- ")
person["city"] = input("Enter your city :- ")

print("now see oue Updated Dictionary :- ", person)

check = input("\nEnter a key to check :- ")

if check in person :
    print(check, "exist in the dictionary.")
else:
    print(check, "does not exist in the dictionary.")



print()
#Q9. Practical Application
print("Q9")
print("Write a program to store and manage contact information using a dictionary:")
print()

contacts = {}

name = input("Enter Name :- ")
phone = input("Enter phone number :- ")
email = input("Enter Email :- ")

contacts[name] = {
    "Phone" : phone,
    "Email" : email
}

search = input("\nEnter name to search :- ")

contact = contacts.get(search)
if contact :
    print("\nContact Found :- ")
    print("Phone", contact["Phone"])
    print("Email", contact["Email"])
else :
    print("contact not found.")

print("\nAll Contacts are :- ")
for name, details in contacts.items():
    print("Name :- ", name)
    print("Phone :- ", details["Phone"])
    print("Email :- ", details["Email"])



print()
#Q10. Mini Project - Combined Concepts
print("Q10")
print("Create a Student Management System using a dictionary:")
print()

students3 = {}

while True :
    print("\n==== Student Mangement System ====")
    print("1. Add New Student")
    print("2. Update Marks of a Student")
    print("3. Search Student by roll number")
    print("4. Display All Student")
    print("5. Remove a Student")
    print("6. Exit")

    choice = int(input("Enter your Choice :- "))


    if choice == 1 :
        roll = input("Enter Roll number :- ")
        name = input("Enter Name :- ")
        age = input("Enter age :- ")
        marks = float(input("Enter Marks :-"))


        students3[roll] = {
        "name" : name,
        "age" : age,
        "marks" : marks
        }
        print("Student added successfully!")

    elif choice == 2 :
        roll = input("Enter your roll number :- ")
        student = students3.get(roll)
        if student :
            new_marks = float(input("Enter new marks"))

            students3[roll].update({"marks" : new_marks})
            print("Marks updated Successfully!")
        else :
            print("Student not found")

    elif choice == 3 :
        roll = input("Enter roll number :- ")

        student = students3.get(roll)
        if student :
            print("\nStudent Details")
            print("Name :- ", student["name"])
            print("Age :- ", student["age"])
            print("Marks :- ", student["marks"])
        else:
                print("student not found!")

    elif choice == 4 :
            if len(students3) == 0:
                print("No Student records available.")
            else :
                print("\nAll Student Records")

            for roll, details in students3.items():
                print("\nRoll Number :- ", roll)
                print("Name :- ", details["name"])
                print("age :- ", details["age"])
                print("Marks :- ", details["marks"])

    elif choice == 5 :
        roll = input("Enter Roll Number to Remove :- ")
        removing = students3.pop(roll, None)

        if removing :
            print("Student removed successfully!")
        else :
            print("Student not found!")

    elif choice == 6 :
        print("Exiting Student Management Syatem...")
        break

    else :
        print("Invalid choice! please try again.")

