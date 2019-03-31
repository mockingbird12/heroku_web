import requests
import sys
import json


server = 'http://127.0.0.1:5000/'
# server ='https://flasktest111.herokuapp.com/'
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Not enough args")
        print("Usage: get_all_autors_modules.py [token] autor_id/my_id [id]")
        sys.exit(0)
    api = 'get_all_autors_modules'
    url = server + api
    if 'autor_id' in sys.argv[2]:
        test = {'token':sys.argv[1],'autor_id':sys.argv[3]}
        res = requests.post(url, json=test)
        print("Answer:")
        print(res.text)
        sys.exit(0)
    if 'my_id' in sys.argv[2]:
        test = {'token':sys.argv[1],'my_id':sys.argv[3]}
        res = requests.post(url, json=test)
        print("Answer:")
        print(res.text)
        sys.exit(0)
    else:
        print(sys.argv[2] + " - is wrong")
        print("Usage: get_all_autors_modules.py [token] autor_id/my_id [id]")
        sys.exit(0)