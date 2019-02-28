import requests
import json
def DataCollection():
    dataCollection={
        "test_login_front":{
            'api': 'login_front',
            'login':'sergei',
            'password':"s",
        },
        "test_write_word_to_lesson":{
          'api':'write_word_to_lesson',
          'token':'000',
          'language_from':"ru",
          'language_to':"eng",
          'lesson':'lesson_hello',
          'word':'привет',
          'translate':'hi',
          'comment':'первое слово'},
        "test_change_word":{
            'api': 'change_word_in_lesson',
            'token': '000',
            'id': "1",
            'word': "привет",
            'translate': 'hello',
            "comment":"comment"
        },
        "test_write_answer":{'api': 'write_answer',
                             'token': '000',
                             "word_id":1,
                             "answer":'hello'},
        "test_get_lesson_all_answers": {'api': 'get_lesson_all_answers',
                              'token': '000',
                              "lesson":'ielts_read_1.0',
                              'language_from': 'ru',
                             'language_to': 'eng'},
        "test_get_all_language_autors":{'api': 'get_all_language_autors',
                              'token': '000',
                             'language': 'english'},
        "test_get_all_autors_modules": {'api': 'get_all_autors_modules',
                                         'token': '000',
                                         'autor_id': 1},
        "test_get_all_module_lessons": {'api': 'get_all_module_lessons',
                                        'token': '000',
                                        'autor_id': 1,
                                        'module':"test_module1"},
        "test_get_all_my_modules": {'api': 'get_all_my_modules',
                                        'token': '000',
                                        },
        "test_add_my_module": {'api': 'add_my_module',
                                    'token': '000',
                                    'module':'my_new_module',
                                    'show_module':'yes'
                                    },
        "test_change_module_status": {'api': 'change_module_status',
                               'token': '000',
                               'module': 'my_new_module',
                               'show_module': 'no'
                               },
        "test_add_lesson_to_module": {'api': 'add_lesson_to_module',
                                      'token': '000',
                                      'module': 'my_new_module',
                                      'lesson': 'new_lesson',
                                      'show_lesson':'yes'
                                      },
        "test_change_lesson_status": {'api': 'change_lesson_status',
                                      'token': '000',
                                      'module': 'my_new_module',
                                      'lesson': 'new_lesson',
                                      'show_lesson': 'no'
                                      },
        "test_delete_module": {'api': 'delete_module',
                                      'token': '000',
                                      'module': 'my_new_module',
                                      },
        "test_delete_lesson": {'api': 'delete_lesson',
                               'token': '000',
                               'module': 'my_new_module',
                               'lesson': 'new_lesson',
                               },

        "test_read_lesson": {
            'api': 'read_lesson',
            'token': '000',
            'language_from': "ru",
            'language_to': "eng",
            'module':"test_module1",
            'lesson': 'ielts_read_1.0'},
        "test_check_and_write_answer": {
            'api': 'check_and_write_answer',
            'token': '000',
            'language_from': "ru",
            'language_to': "eng",
            'module':"test_module1",
            'lesson': 'ielts_read_1.0',
            'word_id': 1,
            'translate':'привет',
            'word':'hello',
            'answer':'hello',
           },
        "test_write_word_list_to_lesson": {'api': 'write_word_list_to_lesson',
                                           'token': '000',
                                           'module': 'my_new_module',
                                           'lesson': 'new_lesson',
                                           'language_from': "ru",
                                           'language_to': "eng",
                                           'word_list': [{'word': 'привет',
                                                          'translate': 'hi',
                                                          'comment': 'первое слово'},
                                                         {'word': 'пока',
                                                          'translate': 'bye',
                                                          'comment': 'второе слово'}
                                                         ]
                                           },


    }
    return dataCollection
def Test():
    server = 'http://127.0.0.1:5000/'
    dataCollection=DataCollection()
    testList=["test_login_front",'test_write_word_to_lesson','test_read_lesson','test_change_word',"test_write_answer",'test_get_lesson_all_answers',
              'test_get_all_language_autors',"test_get_all_autors_modules",'test_get_all_module_lessons',
              "test_get_all_my_modules","test_add_my_module","test_change_module_status","test_change_lesson_status",
              "test_delete_module","test_delete_lesson",
              "test_write_word_list_to_lesson",
              'test_read_lesson',"test_check_and_write_answer"]
    #testList=["test_write_word_list_to_lesson"]
    for test in testList:
        data = (dataCollection[test])
        api = data['api']
        url = server + api
        print(url)
        if api=='write_word_list_to_lesson':
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
            res = requests.post(url, json=json.dumps(data), headers=headers)
            resj=res.json()
            print(resj)
            print("______________________________")
        else:
            res = requests.post(url, data=data)
            resj = res.json()
            print(resj)
    # d={                                'api': 'write_word_list_to_lesson',
    #                                    'token': '000',
    #                                    'module': 'my_new_module',
    #                                    'lesson': 'new_lesson',
    #                                    'language_from': "ru",
    #                                    'language_to': "eng",
    #                                    'word_list': [{'word': 'привет',
    #                                                   'translate': 'hi',
    #                                                   'comment': 'первое слово'},
    #                                                  {'word': 'пока',
    #                                                   'translate': 'bye',
    #                                                   'comment': 'второе слово'}
    #                                                  ]
    #                                    },
    #
    # dj=json.dumps(d)
    # print(dj)
    # url=' http://127.0.0.1:5000/test_list'
    # headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    # res = requests.post(url, json=json.dumps(d), headers=headers)



if __name__ == '__main__':
    Test()
