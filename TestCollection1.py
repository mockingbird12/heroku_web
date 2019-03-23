# -*- coding: utf-8 -*-

import requests
import json


def DataCollection():
    dataCollection={
        #проверка идентификации пользователя
        "test_login_front":{
            'api': 'login_front',
            'login':'sergei',
            'password':"s",
        },
        #создать новый модуль AddMyModule(requestform, userid):
       "test_add_my_module": {'api': 'add_my_module',
                               'token': '000',
                                'language_from':'fr',
                                'language_to':'ru',
                                'module':'module6',
                               'show_module':'no' ,
                               'module_comment':'comment module6'
                               },
        "test_add_my_lesson": {'api': 'add_my_lesson',
                               'token': '000',
                               'lesson': 'lesson3',
                               'module_id': '8',
                               'show_lesson': "yes",
                               },
        "test_change_lesson_status": {'api': 'change_lesson_status',
                               'token': '000',
                               'lesson_id': 7,
                               'module_id': 6,
                               'show_lesson': False,
                               },
        # изменить статус модуля ChangeModuleStatus(requestform, user_id)
        "test_change_module_status": {'api': 'change_module_status',
                                      'token': '000',
                                      'module_id': 2,
                                      'show_module': False
                                      },
        "test_change_word_in_lesson": {'api': 'change_word_in_lesson',
                                      'token': '000',
                                      'id': 9,
                                      'word': 'squueze',
                                      'translate': 'кошара'
                                      },

        "test_delete_lesson": {'api': 'delete_lesson',
                               'token': '000',
                               'lesson_id': 9
                               },

    # удалить модуль     DeleteModule(requestform, user_id)
        "test_delete_module": {'api': 'delete_module',
                               'token': '000',
                               'module_id':6
                               },

        "test_get_all_autors_by_language":{'api':'get_all_autors_by_language',
                                           'token':'000',
                                           'language_from':'rus',
                                           'language_to':'eng'
                                },

        "test_get_all_module_lessons":{'api':'get_all_module_lessons',
                                       'token': '000',
                                       'module_id': 9
                                       },
        "test_get_lesson_all_answers":{'api':'get_lesson_all_answers',
                                       'token': '000',
                                       'lesson_id':8
                                       },

        "test_read_lesson":{ 'api':'read_lesson',
                             'token': '000',
                             'lesson_id':5

                            },

        "test_write_wordlist_to_lesson":{ 'api':'write_wordlist_to_lesson',
                                          'token': '000',
                                          'word_list':[{'lesson_id':8, 'word':'word3', 'translate':'перевод3',
                                                        'comment':'comment1'},
                                                       {'lesson_id': 8, 'word': 'word2', 'translate': 'перевод2',
                                                        'comment': 'comment1'},
                                          ]},

        "test_write_word_to_lesson":{ 'api':'write_word_to_lesson',
                                      'token': '000',
                                      'lesson_id':7,
                                      'word':'car',
                                      'translate':'машина',
                                      'word_comment':'комментарий тип машины'
                                    },
        "test_get_all_autors_modules":{'api':'get_all_autors_modules',
                                       'token': '000',
                                       'autor_id': 1,
                                       }
                   }

    return dataCollection


def Test():
    server = 'http://127.0.0.1:5000/'
    # server='https://secure-ravine-71748.herokuapp.com/'
    # server ='https://flasktest111.herokuapp.com/'
    dataCollection=DataCollection()

    # testList=["test_add_my_module","test_delete_module", "test_change_module_status"]
    testList=["test_get_all_autors_modules"]
    for test in testList:
        data = (dataCollection.get(test))
        api = data['api']
        url = server + api
        print(url)
        res = requests.post(url, json=json.dumps(data))
        resj = json.loads(res.text)
        print(resj)
        print("______________________________")

Test()
