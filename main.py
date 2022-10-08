from Classes import Courses, Student

courses = []
students = []
number_of_courses = 0
number_of_students = 0


# The program starts
print("Select Choice Please")
while True:
    try:
        procedure = int(input("""
Pick a number from the following :
1. Add New Student
2. Remove Student
3. Edit Student
4. Display All Students
5. Create New Course.
6. Add Course To Student
0. Exit!\n"""))
    except ValueError:
        print("You should enter the number of the procedure!\n")
        continue

    if procedure == 0:
        break

    # Add New student
    elif procedure == 1:
        student_name = input("Enter Student Name: ")
        student_class = None
        while True:
            student_class = input("Select Student Class (A-B-C)")
            if student_class in ["A", "B", "C"]:
                break
        number_of_students += 1
        students.append(Student(student_name,number_of_students, student_class))
        print("Student Saved Successfully\n")

    # Remove Student
    elif procedure == 2:
        number = int(input("Enter Student id"))
        flag = False
        while True:
            for student in students:
                if student.student_id == number:
                    students.remove(student)
                    print("Deleted Successfully")
                    flag = True
                    break
            if flag == False:
                print("Student Does not existed")
            break

    # Edit Student
    elif procedure == 3:
        number = int(input("Enter Student id"))
        flag = False
        while True:
            for student in students:
                if student.student_id == number:
                    student_name = input("Enter New Name: ")
                    student_class = None
                    while True:
                        student_class = input("Select New Student Class (A-B-C)")
                        if student_class in ["A", "B", "C"]:
                            break
                    student.student_name = student_name
                    student.student_calss = student_class
                    print("Edited Successfully!")
                    flag = True
                    break
            if flag == False:
                print("Student Does not existed\n")
            break

    # Display All Students
    elif procedure == 4:
        for i in students:
            i.student_details()

    # Create New Course
    elif procedure == 5:
        course_name = input("Enter Course Name: ")
        course_class = None
        while True:
            course_class = input("Select Course Class (A-B-C)")
            if course_class in ["A", "B", "C"]:
                break
        number_of_courses += 1
        courses.append(Courses(number_of_courses, course_name, course_class))



    # Add Course To Student
    elif procedure == 6:
        number = int(input("Enter Student id"))
        student_flag = False
        course_flag = False
        while True:
            for student in students:
                if student.student_id == number:
                    course_name = input("Enter Course Name: ")
                    for course in courses:
                        if course.course_name == course_name:
                            student.add_course(course)
                            course_flag = True
                    if course_flag == False:
                        print("Course Does not existed\n")
                    student_flag = True
                    break
            if student_flag == False:
                print("Student Does not existed\n")
            break