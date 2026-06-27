#Q1. Basic try-except
print("Q1")
print("Write a program that takes two numbers as input from the user and prints their\ndivision.\nUse try-except to handle the case when the user enters non-numeric input\n(ValueError).\nPrint a friendly message if an error occurs.")
print()

try :
    n1 = float(input("Enter first value :- "))
    n2 = float(input("Enter second value :- "))

    div = n1 / n2
    print("Division :- ", div)

except ValueError :
    print("Please enter valid numeric values.")


print("\n")
#Q2. Handling ZeroDivisionError
print("Q2")
print("Write a program that divides two numbers entered by the user.\nUse try-except to specifically catch ZeroDivisionError and print:\n'Error: Division by zero is not allowed.'\nAlso handle ValueError for invalid input.")
print()

try :
    n1 = float(input("Enter first value :- "))
    n2 = float(input("Enter second value :- "))

    div = n1 / n2
    print("Division :- ", div)

except ZeroDivisionError :
    print("Error: Division by zero is not allowed.")

except ValueError :
    print("Invalid input. Please enter number only.")


print("\n")
#Q3. Multiple except Blocks
print("Q3")
print("Create a program that performs division and also tries to convert a string to\ninteger.\nHandle both ValueError and ZeroDivisionError with separate except blocks and\nappropriate messages.")
print()

try :
    n1 = float(input("Enter first value :- "))
    n2 = float(input("Enter second value :- "))

    div = n1 / n2
    print("Division :- ", div)

    text = input("Enter a number as String :- ")
    num = int(text)
    print("Converted Integer = ", num)

except ValueError :
    print("ValueError : Invaid number entered.")

except ZeroDivisionError :
    print("ZeroDvivisionError : Cannot divide by zero.")



print("\n")
#Q4. Using else
print("Q4")
print("Write a program that takes two numbers and divides them.\nUse try, except, and else.\nThe else block should print 'Division performed successfully!' only when no\nexception occurs.")
print()

try :
    n1 = float(input("Enter first value :- "))
    n2 = float(input("Enter second value :- "))

    div = n1 / n2
    print("Division :- ", div)

except ValueError :
    print("ValueError : Invaid number entered.")

except ZeroDivisionError :
    print("ZeroDvivisionError : Cannot divide by zero.")

else :
    print("Division performed successfully!")


print("\n")
#Q5. Using finally
print("Q5")
print("Modify the division program to include a finally block that always prints:\n'Program execution completed.'\nDemonstrate that finally runs whether an exception occurs or not.\nAdd comments explaining the purpose of finally")
print()

try :
    n1 = float(input("Enter first value :- "))
    n2 = float(input("Enter second value :- "))

    div = n1 / n2
    print("Division :- ", div)

except ValueError :
    print("ValueError : Invaid number entered.")

except ZeroDivisionError :
    print("ZeroDvivisionError : Cannot divide by zero.")

finally :
    # This block always execute
    print("Program execution Completed.")



print("\n")
#Q6. Combined try-except-else-finally
print("Q6")
print("Write a complete division program using all four blocks (try, except, else, finally):\nHandle ValueError and ZeroDivisionError.\nPrint success message in else.\nAlways thank the user in finally.")
print()

try :
    n1 = float(input("Enter first value :- "))
    n2 = float(input("Enter second value :- "))

    div = n1 / n2
    print("Division :- ", div)

except ValueError :
    print("ValueError : Invaid number entered.")

except ZeroDivisionError :
    print("ZeroDvivisionError : Cannot divide by zero.")

else :
    print("Division performed successfully!")

finally :
    print("Thank you for using the program.")



print("\n")
#Q7. Practical - Age Input
print("Q7")
print("Write a program that asks the user for their age.\nConvert the input to integer.\nIf the age is negative, raise a ValueError with message 'Age cannot be\nnegative.'\nHandle the exception gracefully and print a suitable message.")
print()

try :
    age = int(input("Enter your agr :- "))

    if age < 0 :
        raise ValueError("Age cannot be negative.")

        print("your age is :- ", age)


except ValueError :
    print("Error : Invalid age entered.")

finally :
    print("Thank you for using the program.")


print("\n")
#Q8. Multiple Exceptions in One Block
print("Q8")
print("Create a program that:\nTakes a number as input.\nDivides 100 by that number.\nHandle both ValueError and ZeroDivisionError in a single except block using a\ntuple.\nPrint a combined error message.")
print()

try :
    n = int(input("Enter a number :- "))

    ans = 100 / n
    print("Answer :- ", ans)

except (ValueError, ZeroDivisionError) :
    print("Invalid input or division by zero.")



print("\n")
#Q9. Debugging Exception Code
print("Q9")
print("The following code has issues. Correct it and add comments explaining the fixes:")
print()

#try
#num = int(input("Enter a number: "))
#result = 100 / num
#print("Result:", result)
#except ValueError
#print("Please enter a valid number")
#except:
#print("Some error occurred")

# There is the perfect code now!
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Some error occurred")




print("\n")
#Q10.Mini Project - Exception Handling
print("Q10")

print()

while True :
    print("+++++++++++ practice mini calculator menu +++++++++++")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try :
        choice = int(input("Enter your choice :- "))
        if choice == 5:
            print("Exiting calculator...")
            break

        num1 = float(input("Enter  first value :- "))
        num2 = float(input("Enter second value :- "))

        if choice == 1:
            print("Answer = ", num1 + num2)
    
        elif choice == 2:
            print("Answer = ", num1 - num2)
    
        elif choice == 3:
            print("Answer = ", num1 * num2)

        elif choice == 4:
            print("Answer = ", num1 / num2)

        else:
            print("Invalid vhoice!")

    except ValueError:
        print("Please enter valid numeric values.")

    except ZeroDivisionError:
        print("Cannot Divide by zero.")

    finally:
        print("mini project complete!")

