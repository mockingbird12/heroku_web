# -*- coding: utf-8 -*-

import json
import os
from flask_cors import CORS
from flask import Flask
from flask import request
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
CORS(app)


@app.route('/index')
def hello_world():
    return 'Hello World!'


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        test=request.form['test']
        outputDataDict={"test":test}
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


#авторизация
@app.route('/login_front', methods=['POST'])
def login_front():
    login=json.loads(request.get_json())["login"]
    password=json.loads(request.get_json())["password"]
    tokenFromUser=GetUserByToken.GetTockenByLoginAndPassword(login,password)
    error=""
    token=""
    if tokenFromUser=='error':
        error="wrong login or password"
    else:
        token=tokenFromUser
    outputDataDict={}
    outputDataDict['token']=token
    outputDataDict['error']=error
    jsonarray = json.dumps(outputDataDict, ensure_ascii=False).encode('utf8')
    jsonarray = jsonarray.decode('utf8')
    return jsonarray


# добавить мой модуль
@app.route('/add_my_module', methods=['POST'])
def add_my_module():
    if request.method == 'POST':
        token = json.loads(request.get_json())['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        data = json.loads(request.get_json())
        outputDataDict=AddMyModule.AddMyModule(data, user_id)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


#добавить урок в модуль
@app.route('/add_my_lesson', methods=['POST'])
def add_lesson_to_module():
    if request.method == 'POST':
        token = json.loads(request.get_json())['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        data = json.loads(request.get_json())
        outputDataDict=AddMyLesson.AddMyLessonByRequstForm(data,user_id)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


#изменить статус урока
@app.route('/change_lesson_status', methods=['POST'])
def change_lesson_status():
    if request.method == 'POST':
        token = json.loads(request.get_json())['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        data = json.loads(request.get_json())
        outputDataDict = ChangeLessonStatus.ChangeLessonStatusByRequestForm(data, user_id)
        print(outputDataDict)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


#изменить статус модуля
@app.route('/change_module_status', methods=['POST'])
def change_module_status():
    if request.method == 'POST':
        token = json.loads(request.get_json())['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        data = json.loads(request.get_json())
        outputDataDict = ChangeModuleStatus.ChangeModuleStatus(data, user_id)
        print(outputDataDict)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray

@app.route('/change_word_in_lesson', methods=['POST']) # not done
def change_word_in_lesson():
    if request.method == 'POST':
        token = json.loads(request.get_json())['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        data = json.loads(request.get_json())
        outputDataDict = ChangeWordInLesson.ChangeWordInLesson(data, user_id)
        print(outputDataDict)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


#проверить и записать ответ
@app.route('/check_and_write_answer', methods=['POST'])
def check_and_write_answer():
    if request.method == 'POST':
        token=request.form['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        if user_id != -1:
            outputDataDict=CheckAndWriteAnswer.CheckAndWriteAnswer(request.form,user_id)
            jsonarray = json.dumps(outputDataDict)
            return jsonarray


#удалить урок
@app.route('/delete_lesson', methods=['POST'])
def delete_lesson():
    if request.method == 'POST':
        token = json.loads(request.get_json())['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        data = json.loads(request.get_json())
        outputDataDict = DeleteLesson.Deletelesson(data, user_id)
        print(outputDataDict)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


#удалить модуль
@app.route('/delete_module', methods=['POST'])
def delete_module():
    if request.method == 'POST':
        token = json.loads(request.get_json())['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        data = json.loads(request.get_json())
        outputDataDict = DeleteModule.DeleteModule(data, user_id)
        print(outputDataDict)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


# все авторы языка
@app.route('/get_all_autors_by_language', methods=['POST'])
def get_all_language_autors():
    if request.method == 'POST':
        token = json.loads(request.get_json())['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        data = json.loads(request.get_json())
        outputDataDict = GetAllModuleLessons.GetAllModuleLessonsByRequstForm(data)
        print(outputDataDict)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray

# все уроки модуля
@app.route('/get_all_module_lessons', methods=['POST'])
def get_all_module_lessons():
    if request.method == 'POST':
        token = json.loads(request.get_json())['token']
        data = json.loads(request.get_json())
        outputDataDict = GetAllModuleLessons.GetAllModuleLessonsByRequstForm(data)
        print(outputDataDict)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray

@app.route('/get_lesson_all_answers', methods=['POST'])
def get_lesson_all_answers():
    if request.method == 'POST':
        token = json.loads(request.get_json())['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        data = json.loads(request.get_json())
        outputDataDict = GetLessonAllAnswers.GetLessonAllAnswers(data)
        print(outputDataDict)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


@app.route('/write_wordlist_to_lesson', methods=['POST'])
def write_word_list_to_lesson():
    if request.method == 'POST':
        token = json.loads(request.get_json())['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        data = json.loads(request.get_json())
        outputDataDict = WriteWordListToLesson.WriteWordListToLesson(data, user_id)
        print(outputDataDict)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


#записать слово в урок
@app.route('/write_word_to_lesson', methods=['POST'])
def write_word_to_lesson():
    if request.method == 'POST':
        token = json.loads(request.get_json())['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        data = json.loads(request.get_json())
        outputDataDict = WriteWordToLesson.WriteWordToLesson(data, user_id)
        print(outputDataDict)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


@app.route('/read_lesson', methods=['POST'])
def read_lesson():
    if request.method == 'POST':
        token = json.loads(request.get_json())['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        data = json.loads(request.get_json())
        outputDataDict = ReadWordsInLesson.ReadLesson(data)
        print(outputDataDict)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray

# write user answer
@app.route('/write_answer', methods=['POST']) # not done
def write_answer():
    if request.method == 'POST':
        return 'api is not created'


# все модули автора
@app.route('/get_all_autors_modules', methods=['POST'])
def get_all_autors_modules():
    if request.method == 'POST':
        token=json.loads(request.get_json())['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        data = json.loads(request.get_json())
        outputDataDict=GetAllAutorsModules.GetAllAoutrosModulesByRequstForm(data)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


# все мои модули
@app.route('/get_all_my_modules', methods=['POST'])
def get_all_my_modules():
    if request.method == 'POST':
        token = json.loads(request.get_json())['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        data = json.loads(request.get_json())
        outputDataDict = GetAllAutorsModules.GetAllAoutrosModulesByRequstForm(data)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


@app.route('/test_list', methods=['POST','GET'])
def test_list():
    if request.method == 'POST':
        print(request.form)
        print(request.args)
        data = request.data
        dataDict = json.loads(data)
        print(dataDict)
        outputDataDict={'test':'test'}
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


from BackendJSON import CheckAndWriteAnswer
from BackendJSON import WriteWordListToLesson
from BackendJSON import DeleteLesson
from BackendJSON import DeleteModule
from BackendJSON import ChangeLessonStatus
from BackendJSON import AddMyLesson
from BackendJSON import WriteWordToLesson
from BackendJSON import ReadWordsInLesson
from BackendJSON import ChangeWordInLesson
from BackendJSON import GetLessonAllAnswers
from BackendJSON import GetAllAutorsByLanguage
from BackendJSON import GetAllAutorsModules
from BackendJSON import GetAllModuleLessons
from BackendJSON import AddMyModule
from BackendJSON import ChangeModuleStatus
from Autorization import GetUserByToken


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    print('App is running')
    app.run()
