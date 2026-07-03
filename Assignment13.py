#Q1. Basic Array Creation
print("Q1")
print("Write a program to:\na) Create a 1D array with elements [10, 20, 30, 40, 50] using np.array().\nb) Create a 2D array (3 x 3) using np.array().\nPrint both arrays along with their shape and data type (dtype).")
print()

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])

print("1D Array:")
print(arr1)
print("Shape:", arr1.shape)
print("Data Type:", arr1.dtype)


arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\n2D Array:")
print(arr2)
print("Shape:", arr2.shape)
print("Data Type:", arr2.dtype)

print("\n")

#Q2. np.zeros() and np.ones()
print("Q2")
print("Create the following using NumPy:\na) A 1D array of 8 zeros.\nb) A 2D array of shape 4, 4) filled with ones.\nc) A 3 3 matrix of zeros.\nPrint all arrays with proper labels.")
print()


arr1 = np.zeros(8)


arr2 = np.ones((4, 4))


arr3 = np.zeros((3, 3))
print("1D Array of 8 Zeros:")
print(arr1)

print("\n4x4 Array of Ones:")
print(arr2)

print("\n3x3 Matrix of Zeros:")
print(arr3)

print("\n")

#Q3 np.arange()
print("Q3")
print("Use np.arange() to create and print the following arrays:\na) Numbers from 0 to 20 (step 1).\nb) Even numbers from 10 to 50.\nc) Numbers from 5 to 100 with step of 5.")
print()



arr1 = np.arange(0, 21, 1)


arr2 = np.arange(10, 51, 2)


arr3 = np.arange(5, 101, 5)


print("Numbers from 0 to 20:")
print(arr1)

print("\nEven Numbers from 10 to 50:")
print(arr2)

print("\nNumbers from 5 to 100 (Step 5):")
print(arr3)

print("\n")


#Q4. np.linspace()
print("Q4")
print("Use np.linspace() to create:\na) 10 equally spaced numbers between 0 and 5.\nb) 15 equally spaced numbers between 10 and 10.\nPrint the arrays and their length.")
print()



arr1 = np.linspace(0, 5, 10)


arr2 = np.linspace(-10, 10, 15)


print("10 Equally Spaced Numbers between 0 and 5:")
print(arr1)
print("Length:", len(arr1))

print("\n15 Equally Spaced Numbers between -10 and 10:")
print(arr2)
print("Length:", len(arr2))


print("\n")
#Q5. Random Arrays
print("Q5")
print("Write a program to generate:\na) A 1D array of 10 random numbers between 0 and 1 using np.random.rand().\nb) A 3 3 matrix of random numbers from standard normal distribution using\nnp.random.randn().\nc) A 2D array 4 5) of random integers between 10 and 50 using\nnp.random.randint().\nPrint all with proper headings.")
print()


arr1 = np.random.rand(10)


arr2 = np.random.randn(3, 3)


arr3 = np.random.randint(10, 51, (4, 5))


print("1D Array of 10 Random Numbers (0 to 1):")
print(arr1)

print("\n3x3 Matrix of Random Numbers (Standard Normal Distribution):")
print(arr2)

print("\n4x5 Array of Random Integers (10 to 50):")
print(arr3)


print("\n")
#Q6. Vectors and Basic Operations
print("Q6")
print("Create two vectors:\nv1 = np.array([2, 4, 6, 8])\nv2 = np.array([1, 3, 5, 7])\nPerform and print:\nAddition\nSubtraction\nElement-wise multiplication\nDot product")
print()


v1 = np.array([2, 4, 6, 8])
v2 = np.array([1, 3, 5, 7])


addition = v1 + v2


subtraction = v1 - v2


multiplication = v1 * v2


dot_product = np.dot(v1, v2)


print("Vector 1:", v1)
print("Vector 2:", v2)

print("\nAddition:")
print(addition)

print("\nSubtraction:")
print(subtraction)

print("\nElement-wise Multiplication:")
print(multiplication)

print("\nDot Product:")
print(dot_product)


print("\n")
#Q7. Matrices and Operations
print("Q7")
print("Create two 3x3 matrices:\nA = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\nB = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])\nPerform the following:\nMatrix addition\nMatrix multiplication (@ or np.dot())\nElement-wise multiplication (*)\nPrint the results clearly.")
print()



A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])


addition = A + B


multiplication = A @ B      # or np.dot(A, B)


elementwise = A * B


print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMatrix Addition:")
print(addition)

print("\nMatrix Multiplication:")
print(multiplication)

print("\nElement-wise Multiplication:")
print(elementwise)


print("\n")
#Q8. Properties of Arrays
print("Q8")
print("Create a 4 4 matrix of random integers between 1 and 100.\nPrint:\nShape\nDimension (ndim)\nTotal number of elements (size)\nData type")
print()



arr = np.random.randint(1, 101, (4, 4))

print("4x4 Random Integer Matrix:")
print(arr)


print("\nShape:", arr.shape)
print("Dimension (ndim):", arr.ndim)
print("Total Number of Elements (size):", arr.size)
print("Data Type:", arr.dtype)
print("Minimum Value:", arr.min())
print("Maximum Value:", arr.max())

print("\n")
#Q9. Combined - Random + Reshape + Statistics
print("Q9")
print("Generate a 1D array of 20 random integers between 1 and 50 using\nnp.random.randint().\nReshape it into a 4 5 matrix.\nPrint the sum, mean, and standard deviation of the matrix.\nFind the maximum value in each row.")
print()


arr = np.random.randint(1, 51, 20)


matrix = arr.reshape(4, 5)


print("4x5 Matrix:")
print(matrix)

print("\nSum:", np.sum(matrix))
print("Mean:", np.mean(matrix))
print("Standard Deviation:", np.std(matrix))

print("\nMaximum Value in Each Row:")
print(np.max(matrix, axis=1))


print("\n")
#Q10. Mini Project - NumPy Application
print("Q10")
print("Mini Project")


try:
    
    n = int(input("Enter how many random numbers you want to generate: "))

    if n <= 0:
        print("Please enter a positive number.")

    else:
        
        arr = np.random.randint(10, 101, n)

        
        print("\nGenerated Array:")
        print(arr)

        
        print("\nMean:", np.mean(arr))
        print("Median:", np.median(arr))
        print("Standard Deviation:", np.std(arr))
        print("Minimum:", np.min(arr))
        print("Maximum:", np.max(arr))

        
        if n % 2 == 0:
            matrix = arr.reshape(n // 2, 2)

            print("\nReshaped 2D Array:")
            print(matrix)

            print("\nRow-wise Sum:")
            print(np.sum(matrix, axis=1))

        else:
            print("\nCannot reshape into a 2D array with 2 columns because the number of elements is odd.")

except ValueError:
    print("Invalid input! Please enter an integer only.")

