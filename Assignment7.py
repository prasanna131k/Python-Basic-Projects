#Q1. Creating Tuples
print("Q1")
print("Write a program to create tuples using different methods:")
print()

print("a) A tuple with 5 numbers using parentheses.")

tp = (10, 20, 30, 40, 50)
print(tp)

print()

print("b) A mixed tuple containing integer, string, float, and boolean")

tp2 = (10, "strings", 5.5, True)
print(tp2)

print()

print("c) An empty tuple using two different ways.")
print("tuple using parentheses ")
tp3 = ()
print(tp3)

print("tuple using tuple() function")
tp4 = tuple()
print(tp4)

print()

print("d) A single-element tuple with the value 99.")

tp5 = (99,)
print(tp5)

# Rules for single element tuple :- 
# a comma (,) is necessary to create a single element tuple.

print("\n")

#Q2. Tuple Packing
print("Q2")
print("Create a tuple without using parentheses (tuple packing) to store: your name, age, and city.\nPrint the tuple and its type.\nThen unpack the tuple into three separate variables and print them individually.")
print()

tup = ("Prasanna", 18, "Akola")
print(tup)

name, age, city = tup 

print(name)
print(age)
print(city)

print()

#Q3 Indexing and Negative Indexing
print("Q3")
print("Create the tuple: colors = ('red', 'green', 'blue', 'yellow', 'purple', 'orange') Print:\nFirst element\nThird element\nLast element (using negative index)\nSecond last element (using negative index)\nTake an index number as input from the user and print the element at that index.")
print()

colors = ('red', 'green', 'blue', 'yellow', 'purple', 'orange')

print(colors)
print("first element :- ", colors[0])
print("third element :- ", colors[2])
print("last element :- ", colors[-1])

index = int(input("Enter an index number :- "))

print("Element at index", index, "is :- ", colors[index])

print()

#Q4. Slicing Tuples
print("Q4")
print("Given the tuple: numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10) Using slicing, print:\na) Elements from index 2 to 7\nb) First 5 elements\nc) Last 4 elements\nd) Every second element\ne) The entire tuple in reverse order")
print()
# Syntax of slicing,
# tuple[start: stop: step]
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers)

print("elements from 2 to 7 :- ", numbers[2:8])
print('first five elements :- ', numbers[0:6])
print("last four elements :- ", numbers[-4:])
print("entire tuple in revers :- ", numbers[::-1])

print()

#Q5 Nested Tuples
print("Q5")
print("Create a nested tuple to represent a 3 3 matrix:\nmatrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9)) Print:\nThe first row\nThe element at second row, third column\nThe element at third row, first column")
print()

matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("The matrix is :- ", matrix)

print("first row :- ", matrix[0])
print("The  element at second row and third column :- ", matrix[1][2])
print("The element at third row, first column :- ", matrix[2][0])

print()

#Q6 Iterating and Unpacking
print("Q6")
print("Create a tuple: student = ('Rahul', 20, 'Computer Science', 'A')\na) Iterate through the tuple using a for loop and print each item.\nb) Unpack the tuple into four variables (name, age, branch, grade) and print them\nwith descriptive messages.")
print()

student = ('Rahul', 20, 'Computer Science', 'A')
print("tuple :- ", student ,"\n")

print("Item in the tuple :- " )
for item in student :
    print(item)

name, age, branch, grade = student 

print("\n Sudent details : ")
print("name :- ", name)
print("age :- ", age)
print("branch :- ", branch)
print("grade :- ", grade)

print()


#Q7 count() Method
print("Q7")
print("Create the tuple: grades = ('A', 'B', 'A', 'C', 'A', 'B', 'D', 'A', 'B')\nCount and print how many times 'A' appears.\nCount and print how many times 'B' appears.\nTake a grade as input from the user and print how many times it appears.")
print()

grades = ('A', 'B', 'A', 'C', 'A', 'B', 'D', 'A', 'B')
print("The tuple is :- ", grades)
print("how meny times 'A' appears :- ", grades.count('A'))
print("how many times 'B' appears :- ", grades.count('B'))

grade = input("Enter a grade :- " ).upper()

print("number of", grade, "'s :- ", grades.count(grade))

print()

#Q8 index() Method
print("Q8")
print("Create the tuple: fruits = ('apple', 'banana', 'cherry', 'banana', 'mango', 'apple')\nFind and print the first index of 'banana'.\nFind and print the first index of 'banana' starting the search from index 2.\nUse try-except to safely find the index of 'kiwi' and print 'Not found' if it doesn't exist.")
print()

fruits = ('apple', 'banana', 'cherry', 'banana', 'mango', 'apple')
print(fruits)
print("First index of banana :- ",fruits.index('banana'))
print("First index of banana from index 2 :- ", fruits.index('banana', 2))

try:
    print("index of kiwi :", fruits.index('kiwi'))
except ValueError:
    print("not found")

print()


#Q10 
print("Q10")
print("Mini Project - Combined Concepts")
print()

# Taking input fro Student1
print("Student info")
name = input("Enter Studend name :- ")
roll_no = int(input("Enter roll no :"))

print("sub maarks :")
mark1 = int(input("Enter mark 1 : "))
mark2 = int(input("Enter mark 2 : "))
mark3 = int(input("Enter mark 3 : "))

# Packing all information into a tuple
student1 = (name,  roll_no, mark1, mark2, mark3)

# printing the all record
print("\nStudent Record :")
print(student1)


# unpacking the tuple
name, roll_no, mark1, mark2, mark3 = student1

# Printing unpacking values with labels
print("\nStudent Details")
print("Name             :", name)
print("Roll_no          :", roll_no)
print("Mark 1           :", mark1)
print("Mark 2           :", mark2)
print("Mark 3           :", mark3)

# Using count() function to chack how many times a particular maeks appears
search_mark = int(input("\nEnter a mark to count :"))
print("The mark", search_mark, "appears", student1.count(search_mark), "time(s).")

# creating another student record 
student2 = ("priya", 102, 85, 90, 88)

# creating a nested tuple to store multiple student records
students = (student1, student2)

# printing all students records
print("\nAll Student Record ")
print(students) 
#Accessing specific values from the nested tuple
print("\nAccessing Specific value : ")
print("First Student Name :- ", students[0][0])
print("Second Student Roll Number :- ", students[1][1])
print("Second Student Mark 1 :- ", students[1][2])

print()


#Q9 Immutability of Tuples
print("Q9")
print("Create a tuple: coordinates = 10, 20\nDemonstrate that tuples are immutable by trying to:\nChange the first element\nAdd a new element using append()\nExplain what errors occur (in comments). Then show the correct way to modify\ndata by converting the tuple to a list, making changes, and converting back to a tuple.")
print()

coordinates = (10, 20)
print("Original tuple :- ", coordinates)
# tuple are imutable (cannot be changed)

# Trying to change the first element
# coordinates[0] = 100
# Error: TypeError
# Message: 'tuple' object does not support item assignment

# Trying to add a new element using append()
# coordinates.append(30)
# Error: AttributeError
# Message: 'tuple' object has no attribute 'append'

# Correct way to modify a tuple:
# Step 1: Convert the tuple to a list
temp_list = list(coordinates)

# Step 2: Make changes
temp_list[0] = 100
temp_list.append(30)

# Step 3: Convert the list back to a tuple
coordinates = tuple(temp_list)

# Printing the modified tuple
print("Modified Tuple:", coordinates)