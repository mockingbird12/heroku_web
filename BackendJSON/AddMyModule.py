from TestDataForFrontEnd import modules
def GetAllAoutrosModulesByRequstForm(requestform,user_id):
    module=requestform['module']
    show_module=requestform['show_module']
    str="module: "+module+","+"show_module: "+show_module
    outputDataDict={"status":str,
                    "error":""}
    return outputDataDict
