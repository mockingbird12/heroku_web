from BackendJSON.DatabaseDriver import Answers

answers = Answers()

def WriteAnswer(requestform, user_id):
    error = answers.insert(requestform, user_id)
    status = 'user: ' + str(user_id) + ' write word_id: ' + str(requestform['word_id']) + ' error:' + error
    return status