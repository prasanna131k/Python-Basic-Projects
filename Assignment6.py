#Q1. Creating lists



print('Q1')
print('Write a program to create the following lists using different methods:\na) A list of 5 integers directly.\nb) An empty list using both [] and list().\nc) A list containing mixed data types (int, string, float, boolean).\nd) A list of 7 zeros using repetition (*).')
print()

# a)
a = [10, 20, 30, 40, 50]

#b)
b = []
B = list()

#c)
mix = [10, 5.5, "string", False]

#d)
count = [0] * 7

print('a) 5 int list :-', a)
print('b) Empty list using []:- ', b)
print('   Empty list using list() function :- ', B)
print('c) mix data type list :- ', mix)
print('d) list of 7 zeros :- ', count)

print('\n')



#Q2. Indexing and Negative Indexing
print('Q2')
print('Create a list: fruits = ["apple", "banana", "mango", "orange", "grape"] Write code to print:\nFirst item\nThird item\nLast item (using negative index)\nSecond last item (using negative index)')
print()
fruits = ["apple", "banana", "mango", "orange", "grape"]
print('First item :- ', fruits[0])
print('Third item :- ', fruits[2])
print('Last item :- ', fruits[-1])
print('Second last item :- ', fruits[-2])

index = int(input('Enter an index number (range 0 to 4) :- '))
if index >= 0 and index < len(fruits):
    print('Item at index ', index,'is :-', fruits[index])
else:
    print('Invalid index!')

print()



#Q3. Slicing Lists
print('Q3')
print('Given the list: numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] Using slicing, print:\na) First 4 elements\nb) Last 3 elements\nc) Elements from index 2 to 7\nd) Every second element\ne) The entire list in reverse order')
print()


num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Syntax: list[start:end]
# Elements from index 0 to 3
print('a) first 4 elements :- ', num[3])
# Negative indexing starts from the end
print('b) Last 3 elements :- ', num[-3:])
# Includes index 2, excludes index 8
print('c) Elements from index 2 to 7 :- ', num[2:8])
# Syntax: list[start:end:step]
# Step value of 2 selects every second element
print('d) Every second element :-', num[::2])
# Step value of -1 reverses the list
print('e) The entire list in reverse order :- ', num[::-1])

print()


#Q4. Modifying Lists
print('Q4')
print('Create a list: colors = ["red", "blue", "green", "yellow"] Perform the following:\nChange "blue" to "purple" using indexing.\nChange the last item to "black".\nPrint the list after each change.')
print()

colors = ["red", "blue", "green", "yellow"]

print('original list :- ', colors)

colors[1] = "purple"
colors[-1] = "black"

print('Print the list after each change :- ', colors)

print()


#Q5. append() and insert()
print('Q5')
print('Write a program that starts with an empty list.\nUse append() to add 5 different city names one by one.\nUse insert() to add one more city at position 2.\nPrint the final list.\nTake user input for at least 2 cities.')
print()


cities = []

city1 = input("Enter first city: ")
city2 = input("Enter second city: ")

cities.append(city1)
cities.append(city2)
cities.append("Mumbai")
cities.append("Delhi")
cities.append("Chennai")

new_city = input("Enter a city to insert at position 2: ")
cities.insert(2, new_city)

print("\nFinal List of Cities:")
print(cities)

print()


#Q6. remove(), pop(), and clear()
print('Q6')
print('Create a list: items = [10, 20, 30, 20, 40, 50] Perform and print after each operation:\na) Remove the first occurrence of 20 using remove().\nb) Remove the item at index 3 using pop() and print the removed value.\nc) Remove the last item using pop().\nd) Clear the entire list using clear().')
print()


items = [10, 20, 30, 20, 40, 50]

print("Original List:", items)

# a) remove() removes the first occurrence of a specified value
items.remove(20)
print("After remove(20):", items)

# b) pop(index) removes and returns the item at the given index
removed_item = items.pop(3)
print("Removed value using pop(3):", removed_item)
print("List after pop(3):", items)

# c) pop() without an index removes and returns the last item
last_item = items.pop()
print("Removed last item:", last_item)
print("List after removing last item:", items)

# d) clear() removes all items from the list
items.clear()
print("List after clear():", items)

# Difference:
# remove(value) removes an item by its value.
# pop(index) removes an item by its index and returns the removed item.

print()

#Q7. (index() and count())
print('Q7')
print('Create a list: scores = [85, 92, 78, 92, 65, 92, 88]\nFind and print the index of the first occurrence of 92.\nCount and print how many times 92 appears.\nTake a number as input from the user and check if it exists in the list. If yes,\nprint its index and count.')
print()

scores = [85, 92, 78, 92, 65, 92, 88]

print("Index of first occurrence of 92:", scores.index(92))

print("Count of 92:", scores.count(92))

number = int(input("Enter a number to search: "))

if number in scores:
    print(number, "exists in the list.")
    print("First Index:", scores.index(number))
    print("Count:", scores.count(number))
else:
    print(number, "does not exist in the list.")

print()


#Q8. sort() and reverse()
print('Q8')
print('Create a list: marks = [45, 78, 65, 90, 34, 82, 71]\nSort the list in ascending order and print it.\nSort the list in descending order and print it.\nReverse the original list (without sorting) and print it.')
print()

marks = [45, 78, 65, 90, 34, 82, 71]
print("Original List:", marks)

ascending_marks = marks.copy() 
print("Ascending Order:", ascending_marks)

descending_marks = marks.copy() 
print("Descending Order:", descending_marks)

reversed_marks = marks.copy()
print("Reversed Original List:", reversed_marks)

print()



#Q9 extend() vs append()
print('Q9')
print('Create two lists:\nlist1 = [1, 2, 3]\nlist2 = [4, 5, 6]\na) Using extend() to add list2 to list1.\nb) Using append() to add list2 to a copy of list1.')
print()

list1 = [1, 2, 3]
list2 = [4, 5, 6]

extend_list = list1.copy()
extend_list.extend(list2)

print("Using extend():", extend_list)

append_list = list1.copy()
append_list.append(list2)

print("Using append():", append_list)

# Difference:
# extend() adds individual elements of another list.
# append() adds the entire list as one single element at the end.

print()



#Q10. Mini Project - Combined Concepts
print('Q10')
print()
marks_list = []

# Taking marks for 5 subjects from the user
for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks_list.append(mark)

# Displaying the list of marks
print("\nMarks List:", marks_list)

# Adding one more subject mark using append()
extra_mark = float(input("Enter marks for one more subject: "))
marks_list.append(extra_mark)

print("Updated Marks List:", marks_list)

# Finding and displaying highest and lowest marks
print("Highest Marks:", max(marks_list))
print("Lowest Marks:", min(marks_list))

# Sorting marks in descending order
marks_list.sort(reverse=True)
print("Marks in Descending Order:", marks_list)

# Calculating average marks
total_marks = sum(marks_list)
average_marks = total_marks / len(marks_list)

print("Average Marks:", average_marks)

# Displaying total number of subjects
print("Total Number of Subjects:", len(marks_list))









