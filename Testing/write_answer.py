import requests
import sys
import json


server = 'http://127.0.0.1:5000/'
# server ='https://flasktest111.herokuapp.com/'
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Not enough args")
        print("Usage: write_answer.py [token] [lesson_id] [word_id] [answer]")
        sys.exit(0)
    api = 'write_answer'
    test = {'token':sys.argv[1], 'lesson_id':sys.argv[2], 'word_id': sys.argv[3], 'answer': sys.argv[4]}
    url = server + api
    res = requests.post(url, json=test)
    print("Answer:")
    print(res.text)