class Lecture:
    def __init__(self, title, content):
        self.title = title
        self.content = content  # текст або посилання

    def view(self):
        return self.content
