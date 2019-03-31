import requests
import sys
import json


server = 'http://127.0.0.1:5000/'
# server ='https://flasktest111.herokuapp.com/'
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Not enough args")
        print("Usage: change_module_status.py [token] [module_id] [show_module]")
        sys.exit(0)
    api = 'change_module_status'
    test = {'token':sys.argv[1], 'module_id':sys.argv[2], 'show_module':sys.argv[3]}
    url = server + api
    res = requests.post(url, json=test)
    print("Answer:")
    print(res.text)