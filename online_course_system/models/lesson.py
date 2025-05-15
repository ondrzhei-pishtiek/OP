from models.lecture import Lecture
from models.task import Task

class Lesson:
    def __init__(self, title):
        self.title = title
        self.lectures = []
        self.tasks = []

    def add_lecture(self, lecture):
        self.lectures.append(lecture)

    def add_task(self, task):
        self.tasks.append(task)

    def is_complete(self):
        return bool(self.lectures) and bool(self.tasks)
