# GPA Code

# For All Semester
sem = int(input('How many semester you take? '))
ver = int(input('How many summer semester you take? '))
Semester = []


# Verify grade
def verifyGrade(g):
    if g == 'a' or g == 'A':
        return 'A'
    elif g == 'b' or g == 'B':
        return 'B'
    elif g == 'c' or g == 'C':
        return 'C'
    elif g == 'd' or g == 'D':
        return 'D'
    elif g == 'f' or g == 'F':
        return 'F'
    elif g == 'p' or g == 'P':
        return 'P'
    else:
        return "None"


# Creating list for All Semester
totalCredit = 0
totalForPassCredit = 0
totalGradeCredits = 0

w = 0
while w < sem + ver:
    if w < sem:
        Semester.append('Semester ' + str(w + 1))
        print('Semester ' + str(w + 1))
    else:
        Semester.append('Summer Semester ' + str(w - sem + 1))
        print('Summer Semester ' + str(w - sem + 1))

    # Name of the class
    numClass = int(input('Number of class: '))
    className = []
    classCredit = []
    classGrade = []

    # Creating list of class, class credit and class grade
    i = 0
    while i < numClass:
        className.append(input('Name of class ' + str(i + 1) + ': '))
        classCredit.append(input('Credit of class ' + str(i + 1) + ': '))
        i += 1

    print("List of Class: " + str(className))
    print("List of Credits: " + str(classCredit))

    i = 0
    while i < numClass:

        grade = input('Grade of class ' + str(i + 1) + ': ')
        if verifyGrade(grade) != 'None':
            classGrade.append(verifyGrade(grade))
            i += 1
        else:
            print("Error!! Grade not defined")

    print("List of Grade: " + str(classGrade))

    # Total of Credit
    for i in range(len(classCredit)):
        totalCredit += int(classCredit[i])

    # Total of Grade by Credit
    for i in range(len(classGrade)):
        if classGrade[i] == 'A':
            totalGradeCredits += 4 * int(classCredit[i])
        elif classGrade[i] == 'B':
            totalGradeCredits += 3 * int(classCredit[i])
        elif classGrade[i] == 'C':
            totalGradeCredits += 2 * int(classCredit[i])
        elif classGrade[i] == 'D':
            totalGradeCredits += 1 * int(classCredit[i])
        else:
            totalGradeCredits += 0 * int(classCredit[i])

    # Rearrange lists
    sumList = []

    for i in range(len(className)):
        result = ["Class: " + className[i], "Credit: " + classCredit[i], "Grade: " + classGrade[i]]
        # Adding Pass Credit
        if classGrade[i] == 'P':
            totalForPassCredit += classCredit[i]

        sumList.append(str(result))

    sumList = '\n'.join(sumList)
    Semester.append(sumList)
    w += 1

# Print Semester List
Semester = '\n'.join(Semester)
print(Semester)
print("Total of Credit: " + str(totalCredit))

# Total GPA
gpaScore = totalGradeCredits / (totalCredit - totalForPassCredit)
gpaTotal = round(gpaScore, 3)

print('Total GPA: ' + str(gpaTotal))
