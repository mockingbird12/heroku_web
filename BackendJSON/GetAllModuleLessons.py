from BackendJSON.DatabaseDriver import Lessons

lessons = Lessons()

def GetAllModuleLessonsByRequstForm(requestform):
    module_id = requestform['module_id']
    return (lessons.select_by_module(module_id))