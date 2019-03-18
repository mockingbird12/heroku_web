from BackendJSON.DatabaseDriver import Modules

modules = Modules()

def ChangeModuleStatus(requestform,user_id):
    show_module = requestform['show_module']
    module_id = requestform['module_id']
    res = modules.update(show_module, module_id)
    status = 'user ' + str(user_id) + ' change:' + str(module_id) + ' status to: ' + str(show_module)
    if res != '':
        status = 'action not complete'
        outputDataDict = {"error": res}
    else:
        print(res)
        outputDataDict = {"status": status}
    return outputDataDict
