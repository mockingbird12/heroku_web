from Autorization import GetUserByToken
from JSONRequest import ReadJson
from JSONRequest import config
from JSONRequest.DatabaseDriver import Words
import json

words_db = Words()

def ChangeWordInLesson1(requestform, user_id):
    res = words_db.update(requestform)
    if res == '':
        word = requestform['word']
        translate = requestform['translate']
        result = 'change to' + word + ", " + translate
        outputDataDict = {"resust": result}
    else: outputDataDict = {"resust": res}
    return outputDataDict


def ChangeWordInLesson(requestform,user_id):
    #print(requestform)
    word_id=int(requestform['id'])
    translate=requestform['translate']
    word=requestform['word']
    comment=requestform['comment']
    #print(token,user_id,word_id,translate,word,comment)
    fname = config.path
    data = ReadJson.ReadJson(fname)
    #print(data)
    for d in data:
        curId=d['id']
        user=d['user_id']
        if curId==word_id and user_id==user:
            d['word']=word
            d['translate']=translate
            d['comment']=comment

    with open(fname, mode='w') as f:
        f.write(json.dumps(data))
    result = 'change to' + word+", "+translate
    outputDataDict = {"resust": result}
    return  outputDataDict


def Test():
    fname = config.path
    data = ReadJson.ReadJson(fname)
    print(data)


if __name__ == '__main__':
    Test()
