from JSONRequest.DatabaseDriver import Answers

answers = Answers()

def CheckAndWriteAnswer(requestform,user_id):
    word_id = requestform['word_id']
    answers_user = requestform['answer']  # from user
    error = answers.insert(requestform)
    status = ''
    right_answer = 'no'
    if requestform['translate'] == requestform['answer']:
        right_answer = 'yes'
    status = 'user: ' + str(requestform['user_id']) + ' write word_id: ' + str(requestform['word_id']) + ' answer: ' \
             + right_answer + ' error:' + error
    return status