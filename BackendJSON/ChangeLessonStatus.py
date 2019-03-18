from BackendJSON.DatabaseDriver import Lessons

lessons = Lessons()

def ChangeLessonStatusByRequestForm(requestform,user_id):
    lesson_id = requestform['lesson_id']
    show_lesson = requestform['show_lesson']
    module = requestform['module_id']
    status = 'user ' + str(user_id) + ' change: ' + str(module) + ' ,lesson ' + str(lesson_id) + ' status to: ' + str(
        show_lesson)
    res = lessons.update(show_lesson, lesson_id)
    if res != '':
        status = 'action not complete'
        outputDataDict = {"status": status,"error": res}
    else:
        print(res)
        outputDataDict = {"status": status}
    return outputDataDict
