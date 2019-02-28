from TestDataForFrontEnd import modules
def GetAllAoutrosModulesByRequstForm(requestform):
    author_id=requestform['autor_id']
    allmodules = modules.modules
    user_modules = allmodules[author_id]
    return user_modules
