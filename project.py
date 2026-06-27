
students = {}


# Function to add student
def add_student():
    roll = int(input("Enter Roll Number: "))

    if roll in students:
        print("Roll Number already exists!")
        return

    name = input("Enter Student Name: ")

    marks = []
    print("Enter Marks of 5 Subjects")

    for i in range(5):
        mark = float(input(f"Subject {i+1}: "))
        marks.append(mark)

    percentage = sum(marks) / 5
    grade = calculate_grade(percentage)

    students[roll] = {
        "name": name,
        "marks": marks,
        "percentage": percentage,
        "grade": grade
    }

    print("\nStudent Added Successfully!")


# Function to calculate grade
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 35:
        return "Pass"
    else:
        return "Fail"


# Function to display all students
def view_all():
    if len(students) == 0:
        print("No records found.")
        return

    print("\n===== STUDENT RECORDS =====")

    for roll, data in students.items():
        print("--------------------------")
        print("Roll Number :", roll)
        print("Name        :", data["name"])
        print("Marks       :", data["marks"])
        print("Percentage  : %.2f" % data["percentage"])
        print("Grade       :", data["grade"])


# Function to search student
def search_student():
    roll = int(input("Enter Roll Number to Search: "))

    if roll in students:
        data = students[roll]

        print("\nStudent Found")
        print("Name :", data["name"])
        print("Marks :", data["marks"])
        print("Percentage :", "%.2f" % data["percentage"])
        print("Grade :", data["grade"])
    else:
        print("Student not found.")


# Function to update student
def update_student():
    roll = int(input("Enter Roll Number to Update: "))

    if roll not in students:
        print("Student not found.")
        return

    print("1. Update Name")
    print("2. Update Marks")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        new_name = input("Enter New Name: ")
        students[roll]["name"] = new_name
        print("Name Updated Successfully!")

    elif choice == 2:
        marks = []

        print("Enter New Marks")

        for i in range(5):
            mark = float(input(f"Subject {i+1}: "))
            marks.append(mark)

        percentage = sum(marks) / 5
        grade = calculate_grade(percentage)

        students[roll]["marks"] = marks
        students[roll]["percentage"] = percentage
        students[roll]["grade"] = grade

        print("Marks Updated Successfully!")

    else:
        print("Invalid Choice!")



# Function to delete student
def delete_student():
    roll = int(input("Enter Roll Number to Delete: "))

    if roll in students:
        del students[roll]
        print("Student Deleted Successfully!")
    else:
        print("Student not found.")


# Function to display menu
def show_menu():
    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")






while True:
    try:
        show_menu()
        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_all()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_student()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            print("Thank You! Exiting Program...")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please enter valid input.")


