from TestDataForFrontEnd import modules
def GetAllAoutrosModulesByRequstForm(requestform,user_id):
    allmodules = modules.modules
    user_modules = allmodules[str(user_id)]
    return user_modules
