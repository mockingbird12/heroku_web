from BackendJSON.DatabaseDriver import Answers

answers = Answers()

def GetLessonAllAnswers(requestform):
    lesson_id = requestform['lesson_id']
    return answers.read_by_lesson(lesson_id)
