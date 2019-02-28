from JSONRequest import config
from JSONRequest import GetWordById
import json
from datetime import datetime
def WriteAnswer(requestform,user_id):
    word_id=int(requestform['word_id'])
    answer=requestform['answer']
    wordLine=GetWordById.GetWordById(word_id)
    print(wordLine)
    paramList = ['language_from', 'language_to', 'lesson', 'word', 'translate', 'comment']
    fname=config.answersPath
    # read answers file and increase id
    with open(fname) as feedsjson:
        feeds = json.load(feedsjson)
    try:
     lastId=feeds[-1]['id']
     id=lastId+1
    except BaseException:
        id=1
    data = {}
    data['id']=id
    data['user']=user_id
    data['word_id']=word_id
    data['answer']=answer
    dt=datetime.now()
    data['date']=str(dt)
    for p in paramList:
        data[p]=wordLine[p]
    feeds.append(data)
    with open(fname, mode='w') as f:
        f.write(json.dumps(feeds))

    result = 'write ' +answer + " as answer for" + wordLine['translate']
    return result