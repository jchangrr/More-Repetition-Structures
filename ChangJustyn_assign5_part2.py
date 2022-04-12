"""
Assignment #5, Problem #2
Justyn Chang
"""
#ask how many students in class
students = int(input("How many students are in your class? "))
#validate # of students
while True:
    if students <= 0:
        print("Invalid # of students, try again.")
        print()
        students = int(input("How many students are in your class? "))
    else:
        break
#ask how many tests in class
tests = int(input("How many tests in this class? "))
#validate # of tests
while True:
    if tests <= 0:
        print("Invalid # of tests, try again.")
        tests = int(input("How many tests in this class? "))
    else:
        break
print()
print("Here we go!")
print()

#print student #
student_count = 0
total_average = 0
while True:
    student_count += 1
    print("**** Student #", student_count, "****", sep = "")
    test_number = 0
    student_avg = 0
    #ask for tests scores for each student
    while True:
        test_number += 1
        print("Enter score for test #", test_number, sep = "", end = "")
        test_score = float(input(": "))
        #validate test scores
        while True:
            if test_score <= 0:
                print("Invalid score, try again")
                print("Enter score for test #", test_number, sep = "", end = "")
                test_score = float(input(": "))
            else:
                break
        student_avg = student_avg + test_score
        if test_number == tests:
            break
    #calculate test score average for each student
    average = float((student_avg)/tests)
    faverage = format(average, ".2f")
    total_average = total_average + average
    print("Average score for student #", student_count, " is ", faverage, sep = "")
    print()
    if student_count == students:
        break

#calculate total average for class
total_average = format(float(total_average / students), ".2f")
print("Average score for all students is: ", total_average)
