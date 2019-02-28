from Autorization import GetUserByToken
from JSONRequest import ReadJson
from JSONRequest import config
import json
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
