import json
from JSONRequest import config
from Autorization import GetUserByToken
from JSONRequest import ReadJson
def ReadLesson(requestform,user_id):
        language_from=requestform['language_from']
        language_to = requestform['language_to']
        lesson = requestform['lesson']
        fname=config.path
        data=ReadJson.ReadJson(fname)
        print(data)
        lessonData=[]
        for d in data:
            if d['language_from']==language_from and d['language_to']==language_to and d['lesson']==lesson and d['user_id']==user_id:
                lessonData.append(d)
        outputDataDict={"word_list":lessonData}
        return outputDataDict
