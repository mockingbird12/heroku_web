from TestDataForFrontEnd import modules
def GetAllModuleLessonsByRequstForm(requestform):
    author_id=requestform['autor_id']
    module=requestform['module']
    modulesLessons=modules.modulesLessons
    module_Lessons=modulesLessons[author_id][module]
    return  module_Lessons