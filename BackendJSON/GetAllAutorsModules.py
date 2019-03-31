from BackendJSON.DatabaseDriver import Modules

modules = Modules()

def GetAllAoutrosModulesByRequstForm(requestform):
    user_id = None
    if 'autor_id' in requestform:
        user_id=requestform['autor_id']
        return (modules.select_by_user(user_id))
    if 'my_id' in requestform:
        user_id = requestform['my_id']
        return (modules.select_by_user(user_id))
