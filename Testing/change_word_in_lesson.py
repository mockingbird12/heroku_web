import requests
import sys
import json


server = 'http://127.0.0.1:5000/'
# server ='https://flasktest111.herokuapp.com/'
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Not enough args")
        print("Usage: change_word_in_lesson.py [token] [id] [new_word] [translate]")
        sys.exit(0)
    api = 'change_word_in_lesson'
    test = {'token':sys.argv[1], 'id':sys.argv[2], 'word':sys.argv[3], 'translate': sys.argv[4]}
    url = server + api
    res = requests.post(url, json=test)
    print("Answer:")
    print(res.text)