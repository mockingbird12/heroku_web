def Deletelesson(requestform,user_id):
    module=requestform['module']
    lesson=requestform['lesson']
    line='user '+str(user_id)+' delete lesson '+lesson+' from module '+module
    outputDataDict={'status':line,
                    'error':""}
    return outputDataDict