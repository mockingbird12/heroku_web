from TestDataForFrontEnd import modules
def AddMyLessonByRequstForm(requestform,user_id):
    module=requestform['module']
    lesson=requestform['lesson']
    show_lesson=requestform['show_lesson']
    line='user_id '+str(user_id)+' ,add '+lesson + 'in module '+module+', status: '+show_lesson
    outputDataDict={"status":line,"errors":""}
    return  outputDataDict