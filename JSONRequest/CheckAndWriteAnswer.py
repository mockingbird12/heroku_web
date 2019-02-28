def CheckAndWriteAnswer(requestform,user_id):
    outputDataDict={}
    language_from=requestform['language_from']
    language_to=requestform['language_to']
    module=requestform['module']
    lesson=requestform['lesson']
    word_id = int(requestform['word_id'])
    word=requestform['word']
    translate=requestform['translate']
    answer = requestform['answer']
    right_answer='yes'
    line=str(user_id)+' write word_id '+str(word_id)+' answer: '+answer
    outputDataDict['right_answer']=right_answer
    outputDataDict['status']=line
    return outputDataDict