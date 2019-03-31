import requests
import sys
import json


server = 'http://127.0.0.1:5000/'
# server ='https://flasktest111.herokuapp.com/'
if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print("Not enough args")
        print("Usage: login_front.py [user_name] [user_pass]")
        sys.exit(0)
    api = 'login_front'
    test = {'login':sys.argv[1], 'password':sys.argv[2]}
    url = server + api
    res = requests.post(url, json=test)
    print("Answer:")
    print(res.text)