from BackendJSON.DatabaseDriver import Modules

modules = Modules()

def AddMyModule(requestform, user_id):
    error = modules.insert(requestform, user_id)
    if error == '':
        status = 'ok'
    else:
        status = 'error'
    return {"status": status, "error": error}
