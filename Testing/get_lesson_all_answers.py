import requests
import sys
import json


server = 'http://127.0.0.1:5000/'
# server ='https://flasktest111.herokuapp.com/'
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Not enough args")
        print("Usage: get_lesson_all_answers [token] [lesson_id]")
        sys.exit(0)
    api = 'get_lesson_all_answers'
    test = {'token':sys.argv[1],'lesson_id':sys.argv[2]}
    url = server + api
    res = requests.post(url, json=test)
    print("Answer:")
    print(res.text)