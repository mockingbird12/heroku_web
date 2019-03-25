from BackendJSON.DatabaseDriver import Modules

modules = Modules()

def GetAllAoutrosModulesByRequstForm(requestform):
    user_id = None
    if requestform['autor_id']:
        user_id=requestform['autor_id']
    if requestform['my_id']:
        user_id = requestform['my_id']
    return (modules.select_by_user(user_id))
