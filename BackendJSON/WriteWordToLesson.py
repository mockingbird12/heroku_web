from BackendJSON.DatabaseDriver import Words

words = Words()

def WriteWordToLesson(requestform, user_id):
    error = words.insert(requestform)
    status = 'user ' + str(user_id) + ' write word ' + requestform['word']
    if error == '':
        return {"status": status, "error": error}
    else:
        return {"error": error}