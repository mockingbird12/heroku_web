from BackendJSON.DatabaseDriver import Lessons

lessons = Lessons()

def Deletelesson(requestform,user_id):
    lesson_id = requestform['lesson_id']
    error = lessons.delete(lesson_id)
    if error:
        outputDataDict = {'status': 'error','error': error}
    else:
        status = 'user ' + str(user_id) + ' delete lesson ' + str(lesson_id)
        outputDataDict = {'status':status, 'error':""}
    return outputDataDict