import requests
import sys
import json


server = 'http://127.0.0.1:5000/'
# server ='https://flasktest111.herokuapp.com/'
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Not enough args")
        print("Usage: get_all_autors_by_language.py [token] [language_to] [language_from]")
        sys.exit(0)
    api = 'get_all_autors_by_language'
    test = {'token':sys.argv[1],'language_to':sys.argv[2], 'language_from':sys.argv[3]}
    url = server + api
    res = requests.post(url, json=test)
    print("Answer:")
    print(res.text)