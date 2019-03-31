import requests
import sys
import json


server = 'http://127.0.0.1:5000/'
# server ='https://flasktest111.herokuapp.com/'
if __name__ == '__main__':
    if len(sys.argv) < 7:
        print("Not enough args")
        print("Usage: add_my_module.py [token] [language_from] [language_to] [module] [show_module] [module_comment]")
        sys.exit(0)
    api = 'add_my_module'
    test = {'token':sys.argv[1], 'language_from':sys.argv[2], 'language_to':sys.argv[3], 'module':sys.argv[4],
            'show_module': sys.argv[5], 'module_comment': sys.argv[6]}
    url = server + api
    res = requests.post(url, json=test)
    print("Answer:")
    print(res.text)