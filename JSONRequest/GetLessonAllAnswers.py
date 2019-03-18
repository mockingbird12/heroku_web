from JSONRequest.DatabaseDriver import Answers

answers = Answers()

def GetLessonAllAnswers(requestform):
    lesson_id = requestform['lesson_id']
    return answers.read_by_lesson(lesson_id)

def Test():
    requestform={"lesson":'lesson_hello', 'language_from': 'ru', 'language_to': 'eng'}
    lessonList=GetLessonAllAnswers(requestform,1)
    for l in lessonList:
        print(l)

if __name__ == '__main__':
    Test()