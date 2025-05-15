from models.lesson import Lesson
from models.student import Student

class Course:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.lessons = []
        self.students = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def enroll_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def __str__(self):
        return f"Course: {self.title}, Lessons: {len(self.lessons)}, Students: {len(self.students)}"
