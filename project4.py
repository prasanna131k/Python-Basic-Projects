print("===== QUIZ AND EXAMINATION SYSTEM =====")


name = input("Enter Student Name : ")
roll = int(input("Enter Roll Number : "))

# Question Bank (Tuple)
questions = (
    ("Which data type is immutable in Python?",
     "List", "Dictionary", "Tuple", "Set", "C"),

    ("Which keyword is used to define a function?",
     "func", "def", "function", "define", "B"),

    ("Which symbol is used for comments in Python?",
     "//", "#", "/* */", "--", "B"),

    ("Which function is used to take input from the user?",
     "scan()", "cin", "input()", "read()", "C"),

    ("Which collection removes duplicate values?",
     "List", "Tuple", "Set", "Dictionary", "C"),

    ("Which operator is used for exponentiation?",
     "^", "**", "%", "//", "B"),

    ("Which loop is used when the number of iterations is known?",
     "for", "while", "do while", "repeat", "A"),

    ("Which statement is used for decision making?",
     "switch", "if", "goto", "break", "B"),

    ("Which function returns the length of a list?",
     "size()", "count()", "len()", "length()", "C"),

    ("Which keyword is used to create a class?",
     "object", "class", "struct", "define", "B")
)

score = 0
wrong_answers = []

# Display Questions
for i in range(len(questions)):
    print("\nQ", i + 1)
    print(questions[i][0])
    print("A.", questions[i][1])
    print("B.", questions[i][2])
    print("C.", questions[i][3])
    print("D.", questions[i][4])

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == questions[i][5]:
        print("Correct Answer ✓")
        score += 1
    else:
        print("Wrong Answer ✗")
        wrong_answers.append((questions[i][0], questions[i][5]))

# Result
percentage = (score / len(questions)) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Result Report
print("\n========== RESULT REPORT ==========")
print("Student Name :", name)
print("Roll Number  :", roll)
print("Score        :", score, "/", len(questions))
print("Percentage   :", percentage)
print("Grade        :", grade)

if percentage >= 50:
    print("Result       : PASS")
else:
    print("Result       : FAIL")

# Wrong Answers
if len(wrong_answers) > 0:
    print("\nWrong Answer Review")
    for i in range(len(wrong_answers)):
        print("Question :", wrong_answers[i][0])
        print("Correct Answer :", wrong_answers[i][1])
        print()
else:
    print("\nAll answers are correct!")

print("===== THANK YOU =====")