from BackendJSON.DatabaseDriver import Lessons, Modules

modules = Modules()
lessons = Lessons()

def GetAllModuleLessonsByRequstForm(requestform):
    module_id = requestform['module_id']
    return (lessons.select_by_module(module_id))

def GetAllModulesByLanguage(requestform):
    language_to = requestform['language_to']
    language_from = requestform['language_from']
    return (modules.select_by_language(language_from=language_from, language_to=language_to))
