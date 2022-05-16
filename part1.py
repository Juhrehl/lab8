student_names = []
test_grade = []
student_total = []

def main():
    get_info()
    get_avrg()
    get_highest()

def get_info():
    students = int(input("How many students are there? "))
    for i in range(0, students):
        name = str(input("Enter student " + str(i+1) + "'s name: "))
        grades = int(input("Enter a grade: "))
        while (grades < 0):
            grades = int(input("Please re-enter a grade (cannot be negative): "))
        student_names.append(name)
        test_grade.append(grades)

def get_avrg():
    for i in range(0, len(student_names)):
        total = test_grade[i]
        student_total.append(total)
    total_score = 0
    for i in range(0, len(student_names)):
        total_score += student_total[i]
    class_avrg = (total_score / len(student_names))
    print ("Class average: " + str(class_avrg))

def get_highest():
    for i in range(0, len(student_names)):
        print(student_names[i] + "'s total score: " + str(student_total[i]))
    highest_score = 0
    highest_score_pos = 0
    for i in range(0, len(student_names)):
        if student_total[i] > highest_score:
            highest_score = student_total[i]
            highest_score_pos = i
    print("The best student is: " + student_names[highest_score_pos] + " with a grade of " + str(highest_score))

main()
