from BackendJSON.DatabaseDriver import Modules

modules = Modules()

def DeleteModule(requestform,user_id):
    module_id=requestform['module']
    line='user '+str(user_id)+' delete module '+module_id
    error = modules.delete(module_id)
    if error == '':
        outputDataDict={'status':line, 'error':error}
    else:
        outputDataDict={'error': error}
    return outputDataDict

