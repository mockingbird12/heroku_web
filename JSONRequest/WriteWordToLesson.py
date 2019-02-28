import json
from Autorization import GetUserByToken
from JSONRequest import config
def WriteWordToLesson(requestform,user_id):
    language_from = requestform['language_from']
    language_to = requestform['language_to']
    lesson = requestform['lesson']
    word=requestform['word']
    translate=requestform['translate']
    comment=requestform['comment']

    paramList=['language_from','language_to','lesson','word','translate','comment']
    fname=config.path
    with open(fname) as feedsjson:
        feeds = json.load(feedsjson)
    try:
     lastId=feeds[-1]['id']
     id=lastId+1
    except BaseException:
        id=1
    data = {}
    data['id']=id
    data['user_id']=user_id
    for r in requestform:
        if r in paramList:
            data[r] = requestform[r]


    feeds.append(data)
    with open(fname, mode='w') as f:
        f.write(json.dumps(feeds))

    result='write '+word+" "+translate+ ' to '+lesson
    outputDataDict={"result":result}
    return outputDataDict