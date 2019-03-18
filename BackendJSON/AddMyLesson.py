from BackendJSON.DatabaseDriver import Lessons

lessons = Lessons()

def AddMyLessonByRequstForm(requestform,user_id):
    module=requestform['module_id']
    lesson=requestform['lesson']
    show_lesson=requestform['show_lesson']
    error = lessons.insert(requestform)
    if error != '':
        line = 'action not done'
        outputDataDict = {"status": line, "errors": error}
        return outputDataDict
    else:
        line = 'user_id ' + str(user_id) + ' ,add ' + lesson + ' in module ' + module + ', status: ' + show_lesson
        outputDataDict = {"status": line, "errors": ""}
        return outputDataDict
