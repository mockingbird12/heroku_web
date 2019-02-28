def WriteWordToLesson(word,translate,comment):
    line='word '+word+',translate '+translate+'comment '+comment
    return line
def WriteWordListToLesson(requestform,user_id):
    module=requestform['module']
    lesson=requestform['lesson']
    wordlist=requestform['word_list']
    print(wordlist)
    lineList = []
    for w in wordlist:
        word=w['word']
        translate=w['translate']
        comment=w['comment']
        wline=WriteWordToLesson(word,translate,comment)
        line='user ' + str(user_id) + ' write wordlist in '+'module '+module+'lesson '+ lesson+wline
        lineList.append(line)

    outputDataDict={"status":lineList,
                    "error":""}

    return outputDataDict