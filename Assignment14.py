#Q1. Array Properties
print("Q1")
print("Create a 2D array of shape 5, 6) filled with random integers between 10 and 100.\nPrint the following:\nShape of the array\nTotal number of elements (size)\nData type (dtype)")
print()

import numpy as np


arr = np.random.randint(10, 101, (5, 6))


print("2D Array:")
print(arr)

print("\nShape:", arr.shape)
print("Total Number of Elements (size):", arr.size)
print("Data Type:", arr.dtype)

print("\n")
#Q2. Statistical Methods - Basic
print("Q2")
print("Generate a 1D array of 20 random numbers between 1 and 50 using\nnp.random.randint().\nPrint:\nMinimum value and its index (argmin)\nMaximum value and its index (argmax)\nSum of all elements\nMean and Standard Deviation")
print()


arr = np.random.randint(1, 51, 20)


print("Array:")
print(arr)

print("\nMinimum Value:", np.min(arr))
print("Index of Minimum Value:", np.argmin(arr))

print("\nMaximum Value:", np.max(arr))
print("Index of Maximum Value:", np.argmax(arr))

print("\nSum of All Elements:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))


print("\n")
#Q3. Statistical Methods on 2D Array
print("Q3")
print("Create a 4 5 matrix of random integers between 20 and 80.\nFor the entire matrix, print:\nMinimum and maximum value\nSum of all elements\nMean and Standard Deviation\nThen print the sum of each row and each column.")
print()



arr = np.random.randint(20, 81, (4, 5))


print("4x5 Matrix:")
print(arr)


print("\nMinimum Value:", np.min(arr))
print("Maximum Value:", np.max(arr))
print("Sum of All Elements:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))


print("\nSum of Each Row:")
print(np.sum(arr, axis=1))


print("\nSum of Each Column:")
print(np.sum(arr, axis=0))


print("\n")
#Q4. Reshape
print("Q4")
print("Create a 1D array containing numbers from 1 to 24 using np.arange().\nReshape it into 4, 6\nReshape it into 3, 8\nReshape it into 2, 3, 4 3D array)\nPrint all reshaped arrays with their shapes.")
print()


arr = np.arange(1, 25)

print("Original 1D Array:")
print(arr)
print("Shape:", arr.shape)


arr1 = arr.reshape(4, 6)

print("\nArray Reshaped to (4, 6):")
print(arr1)
print("Shape:", arr1.shape)


arr2 = arr.reshape(3, 8)

print("\nArray Reshaped to (3, 8):")
print(arr2)
print("Shape:", arr2.shape)

arr3 = arr.reshape(2, 3, 4)

print("\nArray Reshaped to (2, 3, 4):")
print(arr3)
print("Shape:", arr3.shape)


print("\n")
#Q5. NumPy Indexing - 1D & 2D
print("Q5")
print("Create the following array:\nPython\narr = np.array([[10, 20, 30, 40],\n[50, 60, 70, 80],\n[90, 100, 110, 120]])\nPerform the following indexing:\nExtract first row\nExtract last column\nExtract center 2 2 submatrix\nExtract all even numbers from the array using boolean indexing")
print()



arr = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120]])


print("Original Array:")
print(arr)


print("\nFirst Row:")
print(arr[0])


print("\nLast Column:")
print(arr[:, 3])


print("\nCenter 2x2 Submatrix:")
print(arr[1:3, 1:3])


print("\nEven Numbers:")
print(arr[arr % 2 == 0])


print("\n")
#Q6. Advanced Indexing
print("Q6")
print("Create a 5 5 matrix of random integers between 1 and 100.\nPrint the diagonal elements\nPrint elements greater than 50\nReplace all elements less than 30 with 0\nPrint the modified array")
print()


arr = np.random.randint(1, 101, (5, 5))


print("Original Matrix:")
print(arr)


print("\nDiagonal Elements:")
print(np.diagonal(arr))


print("\nElements Greater Than 50:")
print(arr[arr > 50])


arr[arr < 30] = 0


print("\nModified Matrix:")
print(arr)


print("\n")
#Q7. Arithmetic Operations
print("Q7")
print("Create two arrays:\na = np.array([10, 20, 30, 40])\nb = np.array([1, 2, 3, 4])\nPerform and print:\nAddition, Subtraction, Multiplication, Division\nElement-wise power (**)")
print()



a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])


print("Array a:")
print(a)

print("\nArray b:")
print(b)

print("\nAddition:")
print(a + b)

print("\nSubtraction:")
print(a - b)

print("\nMultiplication:")
print(a * b)

print("\nDivision:")
print(a / b)

print("\nElement-wise Power (a ** b):")
print(a ** b)

print("\nModulo Operation (a % b):")
print(a % b)


print("\n")
#Q8. Matrix Multiplication
print("Q8")
print("Create two 3 3 matrices:\nA = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\nB = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])\nPerform:\nElement-wise multiplication (*)\nMatrix multiplication (@ or np.dot())\nPrint both results and explain the difference in comments.")
print()


A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])


elementwise = A * B


matrix_mul = A @ B      # or np.dot(A, B)


print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nElement-wise Multiplication:")
print(elementwise)

print("\nMatrix Multiplication:")
print(matrix_mul)

# Difference:
# Element-wise multiplication (*) multiplies corresponding elements.
# Matrix multiplication (@ or np.dot()) multiplies rows of A with columns of B.


print("\n")
#Q9. Combined - Properties + Operations + Indexing
print("Q9")
print("Generate a 6 6 matrix of random numbers using np.random.randn().\nPrint its shape, size, and dtype.\nFind the index of the maximum and minimum value.\nExtract the top-left 3 3 submatrix.\nReplace all negative numbers with their absolute value.\nPrint the mean of the modified matrix.")
print()


arr = np.random.randn(6, 6)


print("Original Matrix:")
print(arr)


print("\nShape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)


print("\nIndex of Maximum Value:", np.unravel_index(np.argmax(arr), arr.shape))
print("Index of Minimum Value:", np.unravel_index(np.argmin(arr), arr.shape))


print("\nTop-Left 3x3 Submatrix:")
print(arr[:3, :3])


arr = np.abs(arr)


print("\nModified Matrix (Negative Values Replaced):")
print(arr)


print("\nMean of Modified Matrix:", np.mean(arr))


print("\n")
#Q10. Mini Project - Student Performance Analysis
print("Q10")
print()


marks = np.random.randint(30, 101, (10, 5))

print("Student Marks (10 x 5):")
print(marks)


total = np.sum(marks, axis=1)


average = np.mean(marks, axis=1)


print("\nTotal Marks of Each Student:")
print(total)

print("\nAverage Marks of Each Student:")
print(average)


highest = np.argmax(total)
lowest = np.argmin(total)

print("\nStudent with Highest Total Marks: Student", highest + 1)
print("Total Marks:", total[highest])

print("\nStudent with Lowest Total Marks: Student", lowest + 1)
print("Total Marks:", total[lowest])


print("\nOverall Class Mean:", np.mean(marks))
print("Overall Class Standard Deviation:", np.std(marks))


reshaped = marks.reshape(5, 10)
print("\nReshaped Array (5 x 10):")
print(reshaped)


top3 = np.argsort(total)[-3:][::-1]

print("\nTop 3 Students (Marks in All Subjects):")
print(marks[top3])

