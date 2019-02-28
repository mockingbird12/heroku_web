from JSONRequest import config
from JSONRequest import ReadJson
def GetWordById(_id):
    fname = config.path
    data = ReadJson.ReadJson(fname)
    wordLine={}
    for d in data:
        if d['id']==_id:
            for k in d:
             wordLine[k]=d[k]
    return wordLine
def Test():
    wordLine=GetWordById(1)
    print(wordLine)
if __name__ == '__main__':
    Test()

