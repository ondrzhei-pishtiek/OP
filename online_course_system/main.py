from models.course import Course
from models.lesson import Lesson
from models.lecture import Lecture
from models.task import Task
from models.student import Student
from validators.validators import (
    validate_student_data,
    validate_course_selection,
    validate_lesson_completeness,
)

courses = []
students = []


def create_course():
    """
    Створює новий курс та додає його до загального списку курсів.
    """
    title = input("Введіть назву курсу: ")
    description = input("Опис курсу: ")
    course = Course(title, description)
    courses.append(course)
    print(f"Курс '{title}' створено.\n")


def edit_course():
    """
    Дозволяє редагувати назву та опис існуючого курсу.
    """
    if not courses:
        print("Немає курсів для редагування.\n")
        return

    print("Курси:")
    for i, c in enumerate(courses):
        print(f"{i + 1}. {c.title}")

    index = int(input("Оберіть курс за номером: ")) - 1
    course = courses[index]

    new_title = input(
        "Нова назва курсу (залиште порожнім щоб не змінювати): "
    )
    new_description = input(
        "Новий опис курсу (залиште порожнім щоб не змінювати): "
    )

    if new_title:
        course.title = new_title
    if new_description:
        course.description = new_description

    print("Курс оновлено.\n")


def add_lesson_to_course():
    """
    Додає новий урок з лекцією та завданням до вибраного курсу.
    """
    if not courses:
        print("Спочатку створіть курс.\n")
        return

    print("Доступні курси:")
    for i, c in enumerate(courses):
        print(f"{i + 1}. {c.title}")

    index = int(input("Оберіть курс за номером: ")) - 1
    course = courses[index]

    lesson_title = input("Назва уроку: ")
    lesson = Lesson(lesson_title)

    # Додаємо лекцію
    lec_title = input("Назва лекції: ")
    lec_content = input("Зміст лекції: ")
    lesson.add_lecture(Lecture(lec_title, lec_content))

    # Додаємо завдання
    task_question = input("Введіть формулювання завдання: ")
    task_answer = input("Правильна відповідь: ")
    lesson.add_task(Task(task_question, task_answer))

    if validate_lesson_completeness(lesson):
        course.add_lesson(lesson)
        print(f"Урок '{lesson_title}' додано до курсу '{course.title}'.\n")
    else:
        print("Помилка: урок має містити хоча б одну лекцію і завдання.\n")


def register_student():
    """
    Реєструє нового студента після перевірки коректності даних.
    """
    fname = input("Ім'я: ")
    lname = input("Прізвище: ")
    email = input("Email: ")

    if validate_student_data(fname, lname, email):
        student = Student(fname, lname, email)
        students.append(student)
        print(f"Студента {fname} {lname} зареєстровано.\n")
    else:
        print("Помилка: некоректні дані.\n")


def enroll_student_to_course():
    """
    Записує обраного студента на обраний курс, якщо курс існує.
    """
    if not students:
        print("Немає зареєстрованих студентів.\n")
        return
    if not courses:
        print("Немає доступних курсів.\n")
        return

    print("Студенти:")
    for i, s in enumerate(students):
        print(f"{i + 1}. {s.first_name} {s.last_name}")
    student = students[int(input("Оберіть студента за номером: ")) - 1]

    print("Курси:")
    for i, c in enumerate(courses):
        print(f"{i + 1}. {c.title}")
    course = courses[int(input("Оберіть курс за номером: ")) - 1]

    if validate_course_selection(course.title, courses):
        student.enroll(course)
        print(f"{student.first_name} записаний на курс '{course.title}'.\n")
    else:
        print("Помилка: такого курсу не існує.\n")


def view_student_progress():
    """
    Відображає прогрес обраного студента по всіх курсах.
    """
    if not students:
        print("Немає студентів.\n")
        return

    print("Студенти:")
    for i, s in enumerate(students):
        print(f"{i + 1}. {s.first_name} {s.last_name}")
    student = students[int(input("Оберіть студента за номером: ")) - 1]

    if not student.courses:
        print("Цей студент ще не записаний на курси.\n")
        return

    print("Прогрес студента:")
    for course_title, data in student.courses.items():
        print(f"- {course_title}: {data['progress']}%")


def simulate_lesson_view():
    """
    Імітує перегляд уроку студентом і оновлює прогрес на 10%.
    """
    if not students:
        print("Немає студентів.\n")
        return

    print("Студенти:")
    for i, s in enumerate(students):
        print(f"{i + 1}. {s.first_name} {s.last_name}")
    student = students[int(input("Оберіть студента за номером: ")) - 1]

    if not student.courses:
        print("Цей студент не записаний на жоден курс.\n")
        return

    print("Курси студента:")
    for i, title in enumerate(student.courses):
        print(f"{i + 1}. {title}")
    selected = list(student.courses.keys())[int(input("Оберіть курс: ")) - 1]

    current_progress = student.courses[selected]["progress"]
    if current_progress < 100:
        student.courses[selected]["progress"] = min(100, current_progress + 10)
        print(f"Прогрес оновлено: тепер {student.courses[selected]['progress']}%\n")
    else:
        print("Студент уже завершив цей курс.\n")


def main_menu():
    """
    Виводить головне меню та обробляє вибір користувача.
    """
    while True:
        print("=== Система онлайн-курсів ===")
        print("1. Створити курс")
        print("2. Додати урок до курсу")
        print("3. Редагувати курс")
        print("4. Зареєструвати студента")
        print("5. Записати студента на курс")
        print("6. Переглянути прогрес студента")
        print("7. Переглянути урок (оновити прогрес)")
        print("0. Вийти")

        choice = input("Оберіть дію: ")
        print()
        match choice:
            case "1":
                create_course()
            case "2":
                add_lesson_to_course()
            case "3":
                edit_course()
            case "4":
                register_student()
            case "5":
                enroll_student_to_course()
            case "6":
                view_student_progress()
            case "7":
                simulate_lesson_view()
            case "0":
                print("До зустрічі!")
                break
            case _:
                print("Невірний вибір. Спробуйте ще раз.\n")


if __name__ == "__main__":
    main_menu()
