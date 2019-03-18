from BackendJSON.DatabaseDriver import Words

words = Words()

def WriteWordListToLesson(requestform, user_id):
    word_list = requestform['word_list']
    word_dict = {}
    error = ''
    status = ''
    for w in word_list:
        word_dict.update({'lesson_id': w['lesson_id']})
        word_dict.update({'word': w['word']})
        word_dict.update({'translate': w['translate']})
        word_dict.update({'word_comment': w['comment']})
        try:
            words.insert(word_dict)
            status += status + w['word'] + ' insert '
        except Exception as err:
            status = 'error'
            error = str(err)
    return {"status": status, "error": error}
