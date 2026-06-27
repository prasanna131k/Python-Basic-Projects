#Q1. String indexing
print('Q1')
print('Write a program that takes a string input from the user.')
print()
str = input('Enter an string :- ')

# Take string input from the user
print('The first charactor is :- ', str[0])

# Positive index starts from 0 (left to right)
print('The last charactor is :- ', str[-1])

# Negative index from -1 (right to left)
print('The third charactor from star :-', str[2])

print('The second from the end :- ', str[-2])

print('\n')



#Q2. String slicing
print('Q2')
print('Take a input from the user.\n Using slicing print:- ')
print()

strg = input('Enter an string :- ')

# Slicing syntax: [start:end:step]
# start = starting index (included)
# end = ending index (excluded)
# step = number of positions to move

# a) First 5 characters
print('The frist five charactor is :- ', strg[0:6])

# b) Last 4 charactors
print('The last four charactor is :- ', strg[-4:])

# c) Sring in revers order
print('The string in revers order :- ', strg[::-1])

# d) Every 2nd charactor
print('Every second charactor of the string :- ', strg[::2])

print('\n')



#Q3. String membership
print('Q3')
print('Take a main string and a substring as input from the user \n Chack whether the substring is present in the main string using in and not in. ')
print()

main = input('Enter the main string :-' )
substr = input('Enter the substring to search :- ')

# Chack if the substring is prasent 
if (substr in main):
    print('Substring found!')
else:
    print('substring not found!')

# Check using not
if (substr not in main):
    print('The substring is not  present in the main string.')
else:
    print('The substring is present in the main string.')

# note :
# String membership is case-sensitive.
# For ex, "Python"and "python" are considered differnt.

print()

# Q4. len() function
print('Q4')
print('Take a string as input\n print the length of the string using len().\n prints the last charactor using len() (without using negative index).\n Prints the middle character if the length is odd.')
print()

txt = input('Enter a string :- ')
length = len(txt)

print('Length of the string :- ', length)

print('Last character :- ', txt[length - 1])

if(length %2 != 0):
    middle_index = length // 2
    print('Middle Charactor :- ', txt[middle_index])
else:
    print('The string length is even, so there is no single middle charactor.')

# Common mistakes with len():
# 1. Using text[len(text)] causes IndexError.
#    The last valid index is len(text) - 1.
#
# 2. Forgetting the parentheses:
#    len(text) is correct
#    len is incorrect
#
# 3. Assuming len() starts counting from 0.
#    len() returns the total number of characters, starting from 1.

print()


#Q5. range() - Basic Forms
print('Q5')
print('Write a program using for loop and range() to:\n a) Print numbers from 0 to 10. \n b) Print numbers from 5 to 15. \n c) Print odd numbers from 1 to 21.')
print()

# Forms of range():
# 1. range(stop)
#    Starts from 0 and goes up to (stop - 1)
#
# 2. range(start, stop)
#    Starts from 'start' and goes up to (stop - 1)
#
# 3. range(start, stop, step)
#    Starts from 'start', increases by 'step',
#    and goes up to (stop - 1)

print('Number from 0 to 10 :- ')
for i in range(11):
    print(i, end=' ')
print()

print('Numbers from 1 to 15 :- ')
for i in range(16):
    print(i, end=' ')
print()

print('Odd numbers from 1 to 21 :- ')
for i in range(1, 22, 2):
    print(i, end=' ')


print('\n')


#Q6. range() with Negative Step
print('Q6')
print('Numbers from 20 down to 10 (decreasing). \n Numbers from 15 down to 1 in steps of 2.')
print()

print('Numbers from 20 down to 10 :- ')
for i in range(20, 9, -1):
    print(i, end=' ')
print()

for i in range(15, 0, -2):
    print(i, end=' ')

print('\n')


#Q7. Combined: Strings + range()
print('Q7')
print('Write a program that takes a string from the user.\n Using a for loop and range() with len(), print:\n Each character of the string one by one (with its index).\n The string in reverse order using negative step in range()')
print()

text = input('Enter a string :- ')
print('\nCharacters whit their indices :- ')
for i in range(len(text)):
    print('Index', i, ';', text[i])

print('\nString in reverse order :- ')
for i in range(len(text)- 1, -1, -1):
    print(text[i], end=' ')

print('\n')

#Q8. Mambership with range()
print('Q8')
print('Takes a number as input from the user.\nChecks if the number is present in range(1, 51) and in range(10, 100, 5.')
print()

num = int(input('Enter a number :- '))
if(num in range(1, 51)):
    print(num, 'is present in range(1, 51)')
else:
    print(num, 'is not present in range(1, 51)')

if (num in range(18, 100, 5)):
    print(num, 'is present in range(10, 100, 5)')
else:
    print(num, 'is not present in range(10, 100, 5)')

print()

#Q9. Slicing + range()
print('Q9')
print('Write a program that prints the following using range() and string slicing concepts where applicable:\n First 10 even numbers 2 to 20.\n Numbers from 1 to 30 in steps of 3.\n A string "PythonProgramming" sliced to show "Python", "Programming", and the reverse.')
print()

print('first 10 even numbers :- ')
for i in range(2, 21, 2):
    print(i, end=' ')
print()

print('Numbers from 1 to 30 in steps of 3 :- ')
for i in range(1, 31, 3):
    print(i, end=' ')
print()

sentence = 'PythonProgramming'

print('Python :- ', sentence[:6])
print('Programming ;- ', sentence[6:])
print('Reverse :- ', sentence[::-1])

print()


#Q10. Mini Project - Combined
print('Q10')


user_string = input('Enter a string :- ')

# 1. Print the legth of string
string_length = len(user_string)
print('\nLength of the string :- ', string_length)

# 2. Print first and second half using slicing
middle_index = string_length // 2

print('first half :- ', user_string[:middle_index])
print('second half :- ', user_string[middle_index:])

# 3. Check if the word "Python" is present (case-insensitive)
#Convert the string to lowercase before checking
if 'Python' in user_string.lower():
    print('Python is present in the string.')
else:
    print('Python is not present in the string.')

# 4. Print all characters with their positive and negative indices
print("\nCharacters with Positive and Negative Indices:")

for index in range(string_length):
    negative_index = index - string_length
    print(
        "Character:", user_string[index],
        "| Positive Index:", index,
        "| Negative Index:", negative_index
    )

# 5. Print the string in reverse
print("\nString in Reverse:")

for index in range(string_length - 1, -1, -1):
    print(user_string[index], end="")

print()

# Notes:
# len() returns the total number of characters in the string.
# Slicing syntax: string[start:end:step]
# range(start, stop, step) is used to generate a sequence of numbers.
# lower() converts the string to lowercase for case-insensitive comparison.







