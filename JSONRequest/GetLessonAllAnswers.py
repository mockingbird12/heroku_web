from JSONRequest import config
from JSONRequest import ReadJson
def GetLessonAllAnswers(requestform,user_id):
    lesson=requestform['lesson']
    language_from=requestform['language_from']
    language_to=requestform['language_to']
    fname = config.answersPath
    data = ReadJson.ReadJson(fname)
    lessonList=[]
    for d in data:
        curLesson=d['lesson']
        if user_id==d['user'] and curLesson==lesson and language_from==d['language_from'] and language_to==d['language_to']:
            lessonList.append(d)
    return lessonList

def Test():
    requestform={"lesson":'lesson_hello', 'language_from': 'ru', 'language_to': 'eng'}
    lessonList=GetLessonAllAnswers(requestform,1)
    for l in lessonList:
        print(l)
if __name__ == '__main__':
    Test()