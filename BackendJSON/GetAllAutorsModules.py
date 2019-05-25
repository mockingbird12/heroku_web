from BackendJSON.DatabaseDriver import Modules

modules = Modules()

def GetAllAutorsModulesByRequstForm(requestform, user_id):
    if 'autor_id' in requestform:
        user_id=requestform['autor_id']
        return (modules.select_by_user(user_id))
    else:
        return (modules.select_by_user(user_id))
