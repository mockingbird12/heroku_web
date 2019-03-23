import requests
import json

req = {'api':'get_all_autors_modules', 'token': '000','autor_id': 1}

if __name__ == '__main__':
    server ='https://flasktest111.herokuapp.com/'
    api = req['api']
    url = server + api
    print(url)
    res = requests.post(url, json=json.dumps(req))
    resj = json.loads(res.text)
    for i in resj: print (i)