class Student:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.courses = {}

    def enroll(self, course):
        if course.title not in self.courses:
            self.courses[course.title] = {"progress": 0}
            course.enroll_student(self)

    def update_progress(self, course_title, progress):
        if course_title in self.courses:
            self.courses[course_title]["progress"] = progress
