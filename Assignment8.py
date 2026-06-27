#Q1. Creating Sets
print("Q1")
print("Write a program to create the following sets")
print()

print("a) A set with 5 integers.")

st = {10, 20, 30, 40, 50}
print(st)
print(type(st))

print()

print("b) A set with mixed data types (integer, string, float).")

st = {10, "city", 5.5}
print(st)
print(type(st))

print()

print("c) An empty set using the correct method.")

st = set()
print(st)
print(type(st))

print()


print("d) A set from the string 'hello' using the set() constructor.")


st = set("prasanna131k")
print(st)
print(type(st))

#stes Automatecally reomve duplicate values.
#For ex. in "hello", the latter 'l' twice,
#but a set stores only unique elements, so 'l' appears only once.
#sets do not allow duplicate elements.

print()


#Q2.Characteristics of Sets
print("Q2")
print("Create a set: numbers = {10, 20, 30, 20, 40, 10, 50}\nPrint the set and observe the output.\nDemonstrate that sets are unordered by printing the set multiple times.\nTry to access the first element using indexing (numbers[0 and explain the\nerror in comments.")
print()
numbers = {10, 20, 30, 20, 40, 10, 50}

print(numbers)
print()

print("first print :-", numbers)
print("second print :-", numbers)
print("third print :-", numbers)

# Sets are unordered collections.
# The order of elements is not guaranteed and may differ between executions.

# Trying to access the first element using indexing
# print(numbers[0])

# Error:
# TypeError: 'set' object is not subscriptable
# Explanation:
# Sets do not support indexing because they are unordered.
# Therefore, we cannot access elements using numbers[0], numbers[1], etc.
print()

#Q3.Membership Testing
print("Q3")
print()

print("Takes a set of 5 colors as input from the user\nAsks the user to enter a color name.\nChecks whether the color is present in the set using in and not in.\nPrints appropriate messages")


colors = set()
for i in range (5):
    color = input("Enter a color :- ")
    colors.add(color)
print("\nSet of colors :-", colors)

check_color = input("Enter a color to to chack :- ")

if check_color in colors:
    print(check_color, "is present in the set.")

if check_color not in colors:
    print(check_color, "is not present in the set.")


#Q4.add(), remove(), discard()
print("Q4")
print("Create a set: fruits = {'apple', 'banana', 'mango'}\nPerform the following operations and print the set after each step:")
print()

fruits = {'apple', 'banana', 'mango'}
print("original set is :- ", fruits)

print("a) Add 'orange' using add().")
fruits.add('orange')
print("After adding 'orange' :- ", fruits)

print("b) Add 'banana' again (observe the result).")
fruits.add('banana')
print("After adding 'banana' again :- ", fruits)
#note :-
# 'banana' is already present in the set.
# sets do not allow duplicate element . so no change ocures.

print("c) Remove 'mango' using remove().")
fruits.remove('mango')
print("After removing 'mango.' :- ", fruits)

print("d) Try to remove 'grape' using discard() (no error should occur).")
fruits.discard('grape')
print("After discarding 'grape' :- ", fruits)
# note ;-
# 'grape' is not present in the set.
# discard() does not raise an error if the element is absent.

print("\n")

#Q5. pop() and clear()
print("Q5")
print("Create a set: s = {100, 200, 300, 400, 500}\nUse pop() to remove and print one element.\nPrint the set after popping.\nClear the entire set using clear().\nPrint the final empty set.")
print()

s = {100, 200, 300, 400, 500}
print("original set is :- ", s)

s.pop()
print("after poping :- ", s)

s.clear()
print("after clearing :- ", s)
# Diffiernce between remove(), discard(), and pop()

#remove(element):
#- Remove the specified element.
#- Raises a keyerror if element is not present.
#
# discard(element):
#- Removes the specified element if it exists.
#- Does NOT reise an error if the element is absent.
#
# pop():
#- Remove and returns an arbitrary element from the set.
#- Does not take any argument.
#- Raises s keyerror if the set is emoty.
#


print("\n")


#Q6.update() and copy()
print("Q6")
print("Create two sets:\nset1 = {1, 2, 3}\nset2 = {3, 4, 5, 6}\nMake a copy of set1.\nUpdate set1 with elements from set2 using update().\nPrint both the original copy and the updated set.")
print()

set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

copy = set1.copy()
print("copy of set :- ", copy)

set1.update(set2)
print("Update set :- ", set1)
print("set2 :- ", set2)

print()

#Q7.Union and Intersection
print("Q7")
print("Create two sets:\nA = {1, 2, 3, 4, 5}\nB = {4, 5, 6, 7, 8}\nPrint the union of A and B (using both .union() and operator).\nPrint the intersection of A and B (using both .intersection() and & operator).")
print()

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("set A :- ", A)
print("set B :- ",B)

union1 = A.union(B)
print("\nUnion using .union() :- ", union1)

union2 = A | B
print("Union using | operator :- ", union2)
# Union :
# Combines all union elements from both sets.
# Duplicate elements are include only once.

intersection1 = A.intersection(B)
print("\nIntersection using .intersection() :- ", intersection1)

intersection2 = A & B
print("Intersection using & operator :- ", intersection2)
# Intersection :
# Returns only the element that are common to both sets.

print()


#Q8.Combined Methods
print("Q8")
print("Write a program that:\nTakes 6 numbers as input from the user and stores them in a set (duplicates\nshould be removed automatically).\nAdds two more numbers using add().\nRemoves one number safely using discard().\nPrints the final set and its length using len().")
print()

num = set()

for i in range(6):
    n = int(input(f"Enter number {i + 1} :- "))
    num.add(n)  # Duplicates are removed automatecaly

num1 = int(input("Enter first number to add :- "))
num.add(num1)

num2 = int(input("Enter second number to add :- "))
num.add(num2)

remove_num = int(input("Enter a number to remove :- "))
num.discard(remove_num)

print("\nFinal set :- ", num)
print("Length of set :- ", len(num))


print()

#Q9.Practical Application
print("Q9")
print("Write a program to remove duplicate marks from a list of student scores using a set:\nscores = [85, 92, 78, 92, 85, 88, 95, 78]\nConvert the list to a set.\nPrint the unique scores.\nConvert the set back to a sorted list and print it.\nPrint the total number of unique scores.")
print()

scores = [85, 92, 78, 92, 85, 88, 95, 78]

unique = set(scores)

print("Unique Scores :- ", unique)

sort = sorted(list(unique))

print("Sorted Unique Scores :- ", sort)

print("Total number of unique scores :- ", len(unique))

print()

#Q10.Mini Project - Combined Concepts
print("Q10")
print()

# Creating an empty set to store unique items
items = set()

# Using a while loop to display the menu repeatedly
while True:
    print("\n----- Unique Item Collector Menu -----")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show All Unique Items")
    print("4. Check if an Item Exists")
    print("5. Clear All Items")
    print("6. Exit")

    # Taking user's choice
    choice = int(input("Enter your choice (1-6): "))

    # Option 1: Add an item
    if choice == 1:
        item = input("Enter an item: ")
        items.add(item)
        print(item, "added successfully.")

    # Option 2: Remove an item using discard()
    elif choice == 2:
        item = input("Enter an item to remove: ")
        items.discard(item)
        print(item, "removed (if it existed in the set).")

    # Option 3: Display all unique items
    elif choice == 3:
        print("Unique Items:", items)

    # Option 4: Check whether an item exists
    elif choice == 4:
        item = input("Enter an item to check: ")

        if item in items:
            print(item, "exists in the set.")
        else:
            print(item, "does not exist in the set.")

    # Option 5: Clear all items
    elif choice == 5:
        items.clear()
        print("All items have been cleared.")

    # Option 6: Exit the program
    elif choice == 6:
        print("Exiting the program...")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")