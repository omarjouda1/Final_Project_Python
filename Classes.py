class Courses :
    def __init__(self, course_id, course_name, course_class):
        self.course_id = course_id
        self.course_name = course_name
        self.course_class = course_class

class Student :

    def __init__(self, student_name, student_id, student_class):
        self.student_name = student_name
        self.student_id = student_id
        self.student_class = student_class
        self.student_courses = []

    def add_course(self, new_course):
        if self.student_class == new_course.course_class:
            self.student_courses.append(new_course)
            print("Course Added Successfully to the Student! ")
        else:
            print("Failed to add the Course to Student ")

    def student_details(self):
        print(self.student_name + "\t|\t" + self.student_class + "\t|\t", end="")
        for course in self.student_courses:
            print(course.course_name,end="  ")
        print()