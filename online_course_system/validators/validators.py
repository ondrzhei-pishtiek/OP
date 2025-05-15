def validate_student_data(first_name, last_name, email):
    if not all([first_name, last_name, email]):
        return False
    if "@" not in email or "." not in email:
        return False
    return True

def validate_course_selection(course_title, courses):
    return course_title in [course.title for course in courses]

def validate_lesson_completeness(lesson):
    return lesson.is_complete()
