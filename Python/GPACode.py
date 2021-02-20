# GPA Getter

# For All Semester
sem = input('How many semester you take? ')
ver = input('How many summer semester you take? ')
s = int(sem)
v = int(ver)

Semester = []

# Creating list for All Semester
totalSemesterCreditList = []
totalSemesterGradeCreditList = []
sumListForPass = []

w = 0
while w < s:
    numSem = w + 1
    Semester.append('Semester ' + str(numSem))
    print('Semester ' + str(numSem))

    # Class name
    num = input('Number of class: ')
    x = int(num)

    className = []

    # Creating list of class
    i = 0
    while i < x:
        className.append(input('Name of class ' + str(i + 1) + ': '))
        i += 1

    print("List of Class: " + str(className))

    # Credit
    classCredit = []

    # Creating list of class credit
    i = 0
    while i < x:
        classCredit.append(input('Credit of class ' + str(i + 1) + ': '))
        i += 1

    print("List of Credits: " + str(classCredit))

    # Grade
    classGrade = []

    # Creating list of class grade
    i = 0
    while i < x:

        grade = input('Grade of class ' + str(i + 1) + ': ')
        if grade == 'a' or grade == 'A':
            grade = 'A'
        elif grade == 'b' or grade == 'B':
            grade = 'B'
        elif grade == 'c' or grade == 'C':
            grade = 'C'
        elif grade == 'd' or grade == 'D':
            grade = 'D'
        elif grade == 'f' or grade == 'F':
            grade = 'F'
        elif grade == 'p' or grade == 'P':
            grade = 'P'
        else:
            print("Error!! Grade not defined")
            i -= 1

        classGrade.append(grade)
        i += 1

    print("List of Grade: " + str(classGrade))

    # Total of Credit
    totalCredit = 0
    for i in range(len(classCredit)):
        totalCredit += int(classCredit[i])

    # print("Total of Credit: " + str(totalCredit))

    # Change Grade for number
    numberGrade = []
    for i in range(len(classGrade)):
        if classGrade[i] == 'A':
            numberGrade.append(4)
        elif classGrade[i] == 'B':
            numberGrade.append(3)
        elif classGrade[i] == 'C':
            numberGrade.append(2)
        elif classGrade[i] == 'D':
            numberGrade.append(1)
        else:
            numberGrade.append(0)

    # print(numberGrade)

    # Total of Grade
    gradeCredits = []

    for i in range(len(classCredit)):
        for j in range(len(numberGrade)):
            if i == j:
                result = int(classCredit[i]) * int(numberGrade[i])
                gradeCredits.append(result)

    # Total of Grade by Credit
    totalGradeCredits = 0
    for i in range(len(gradeCredits)):
        totalGradeCredits += int(gradeCredits[i])

    # print("Total of Grade by Credit: " + str(totalGradeCredits))

    # GPA Score
    gpaScore = totalGradeCredits / totalCredit
    gpa = round(gpaScore, 3)

    # Rearrange lists
    sumList = []

    for i in range(len(className)):
        for j in range(len(classCredit)):
            for k in range(len(classGrade)):
                if i == j and i == k and j == k:
                    result = ["Class: " + className[i], "Credit: " + classCredit[j], "Grade: " + classGrade[k]]
                    # Adding Pass Credit
                    if classGrade[k] == 'P':
                        sumListForPass.append(classCredit[j])

                    sumList.append(str(result))

    print(sumListForPass)
    # print(sumList)
    # print("GPA is: " + str(gpa))

    # Submit i Semester to sumList and totals to calculate GPA
    sumList = '\n'.join(sumList)
    Semester.append(sumList)
    totalSemesterCreditList.append(totalCredit)
    totalSemesterGradeCreditList.append(totalGradeCredits)

    w += 1

# Creating list for All Summer Semester
totalSummerCreditList = []
totalSummerGradeCreditList = []
sumListForPassSummer = []

r = 0
while r < v:
    numSem = r + 1
    Semester.append('Summer Semester ' + str(numSem))
    print('Summer Semester ' + str(numSem))

    # Class name
    num = input('Number of class: ')
    x = int(num)

    className = []

    # Creating list of class
    i = 0
    while i < x:
        className.append(input('Name of class ' + str(i + 1) + ': '))
        i += 1

    print("List of Class: " + str(className))

    # Credit
    classCredit = []

    # Creating list of class
    i = 0
    while i < x:
        classCredit.append(input('Credit of class ' + str(i + 1) + ': '))
        i += 1

    print("List of Credits: " + str(classCredit))

    # Grade
    classGrade = []

    # Creating list of class
    i = 0
    while i < x:

        grade = input('Grade of class ' + str(i + 1) + ': ')
        if grade == 'a' or grade == 'A':
            grade = 'A'
        elif grade == 'b' or grade == 'B':
            grade = 'B'
        elif grade == 'c' or grade == 'C':
            grade = 'C'
        elif grade == 'd' or grade == 'D':
            grade = 'D'
        elif grade == 'f' or grade == 'F':
            grade = 'F'
        else:
            print("Error!! Grade not defined")
            i -= 1
            # Fix bug to eliminate the input if is wrong!!

        classGrade.append(grade)
        i += 1

    print("List of Grade: " + str(classGrade))

    # Total of Credit
    totalCredit = 0
    for i in range(len(classCredit)):
        totalCredit += int(classCredit[i])

    # print("Total of Credit: " + str(totalCredit))

    # Change Grade for number
    numberGrade = []
    for i in range(len(classGrade)):
        if classGrade[i] == 'A':
            numberGrade.append(4)
        elif classGrade[i] == 'B':
            numberGrade.append(3)
        elif classGrade[i] == 'C':
            numberGrade.append(2)
        elif classGrade[i] == 'D':
            numberGrade.append(1)
        else:
            numberGrade.append(0)

    # print(numberGrade)

    # Total of Grade
    gradeCredits = []

    for i in range(len(classCredit)):
        for j in range(len(numberGrade)):
            if i == j:
                result = int(classCredit[i]) * int(numberGrade[i])
                gradeCredits.append(result)

    # Total of Grade by Credit
    totalGradeCredits = 0
    for i in range(len(gradeCredits)):
        totalGradeCredits += int(gradeCredits[i])

    # print("Total of Grade by Credit: " + str(totalGradeCredits))

    # GPA Score
    gpaScore = totalGradeCredits / totalCredit
    gpa = round(gpaScore, 3)

    # Rearrange lists
    sumList = []

    for i in range(len(className)):
        if classGrade[i] == 'P':
            sumListForPassSummer.append(classCredit[i])
        result = ["Class: " + className[i], "Credit: " + classCredit[i], "Grade: " + classGrade[i]]
        sumList.append(str(result))

    # print(sumList)
    # print("GPA is: " + str(gpa))

    # Submit i Semester to sumList and totals to calculate GPA
    sumList = '\n'.join(sumList)
    Semester.append(sumList)
    totalSummerCreditList.append(totalCredit)
    totalSummerGradeCreditList.append(totalGradeCredits)

    r += 1

# Union Summer Semester with Semester
totalCreditList = totalSemesterCreditList + totalSummerCreditList
totalGradeCreditList = totalSemesterGradeCreditList + totalSummerGradeCreditList
totalCreditForPass = sumListForPass + sumListForPassSummer

# Print Semester List
Semester = '\n'.join(Semester)
print(Semester)

# Calculating total Credit
totalCredit = 0
for i in range(len(totalCreditList)):
    totalCredit += int(totalCreditList[i])

# Calculating Pass total Credit
totalCreditPass = 0
for i in range(len(totalCreditForPass)):
    totalCreditPass += int(totalCreditForPass[i])

print("Total of Credit: " + str(totalCredit))

# Calculating total of Grades by Credits
totalGradeCredits = 0
for i in range(len(totalGradeCreditList)):
    totalGradeCredits += int(totalGradeCreditList[i])

# print("Total of Grade by Credit: " + str(totalGradeCredits))

# Total GPA
gpaScore = totalGradeCredits / (totalCredit - totalCreditPass)
gpaTotal = round(gpaScore, 3)

print('Total GPA: ' + str(gpaTotal))
