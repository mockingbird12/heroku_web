from BackendJSON.DatabaseDriver import Words

words = Words()

def ReadLesson(requestform):
    lesson_id = requestform['lesson_id']
    return words.select_by_lesson(lesson_id)