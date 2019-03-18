from BackendJSON.DatabaseDriver import Lessons

lessons = Lessons()

def ReadLesson(requestform):
    lesson_id = requestform['lesson_id']
    return lessons.select_by_id(lesson_id)