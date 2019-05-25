from BackendJSON.DatabaseDriver import Words

words_db = Words()

def ChangeWordInLesson(requestform, user_id):
    res = words_db.update(requestform)
    if res == '':
        word = requestform['word']
        translate = requestform['translate']
        result ='user '+ str(user_id) +'change ' + word + ", to " + translate
        outputDataDict = {"result": result}
    else: outputDataDict = {"result": res}
    return outputDataDict

