class Task:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        return self.answer.strip().lower() == user_answer.strip().lower()
