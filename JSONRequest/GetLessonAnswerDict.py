import requests
def GetLessonAnswerDict(server,data):
    url = server + 'get_lesson_all_answers'
    res = requests.post(url, data=data)
    answers = res.json()
    answerDict = {}
    for a in answers:
        word_id = a['word_id']
        if word_id not in answerDict:
            answerDict[word_id] = []
            answerDict[word_id].append(a)
        else:
            answerDict[word_id].append(a)
    return answerDict