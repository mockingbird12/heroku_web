def ChangeLessonStatusByRequestForm(requestform,user_id):
    module = requestform['module']
    lesson=requestform['lesson']
    show_lesson = requestform['show_lesson']
    line ="user "+str(user_id)+ ' change: ' + module +",lesson "+lesson+ ' status to: ' +show_lesson
    outputDataDict = {"status": line,
                      "error": ""}
    return outputDataDict
