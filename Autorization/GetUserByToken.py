from Autorization import autorization_config as config
def GetIdByTocken(token):
    id=-1
    users = config.users
    for u in users:
        if u['token']==token:
            id=u['id']
    return id
def GetTockenByLoginAndPassword(login,password):
    users=config.users
    token = "error"
    for u in users:
        if u['login']==login and u['password']==password:
            token=u['token']
    return token