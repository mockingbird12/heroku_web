import requests
import sys
import json


server = 'http://127.0.0.1:5000/'
# server ='https://flasktest111.herokuapp.com/'
if __name__ == '__main__':
    if len(sys.argv) < 6:
        print("Not enough args")
        print("Usage: write_word_to_lesson.py [token] [lesson_id] [word] [translate] [word_comment]")
        sys.exit(0)
    api = 'write_word_to_lesson'
    test = {'token':sys.argv[1],'lesson_id':sys.argv[2], 'word':sys.argv[3], 'translate':sys.argv[4],
            'word_comment': sys.argv[5]}
    url = server + api
    res = requests.post(url, json=test)
    print("Answer:")
    print(res.text)