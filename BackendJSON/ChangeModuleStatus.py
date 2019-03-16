def ChangeModuleStatus(requestform,user_id):
    show_module=requestform['show_module']
    module=requestform['module']
    line='user '+str(user_id)+' change: '+module+' status to: '+show_module
    outputDataDict={"status":line,
                    "error":""}
    return outputDataDict
