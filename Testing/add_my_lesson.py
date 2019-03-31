import requests
import sys
import json


server = 'http://127.0.0.1:5000/'
# server ='https://flasktest111.herokuapp.com/'
if __name__ == '__main__':
    if len(sys.argv) < 6:
        print("Not enough args")
        print("Usage: add_my_lesson.py [token] [module_id] [lesson] [show_lesson] [lesson_comment]")
        sys.exit(0)
    api = 'add_my_lesson'
    test = {'token':sys.argv[1], 'module_id':sys.argv[2], 'lesson':sys.argv[3], 'show_lesson':sys.argv[4], 'lesson_comment':sys.argv[5]}
    url = server + api
    res = requests.post(url, json=test)
    print("Answer:")
    print(res.text)