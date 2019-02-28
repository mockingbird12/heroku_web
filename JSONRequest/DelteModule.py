def DeleteModule(requestform,user_id):
    module=requestform['module']
    line='user '+str(user_id)+' delete module '+module
    outputDataDict={'status':line,
                    'error':""}
    return outputDataDict

