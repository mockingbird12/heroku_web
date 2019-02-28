# -*- coding: utf-8 -*-

import json
import os
from flask_cors import CORS
from flask import Flask
from flask import request
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
CORS(app)


@app.route('/hello')
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
    login=request.form["login"]
    password=request.form["password"]
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


@app.route('/change_word_in_lesson', methods=['POST'])
def change_word_in_lesson():
    if request.method == 'POST':
        token=request.form['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        if user_id != -1:
            outputDataDict =ChangeWordInLesson.ChangeWordInLesson(request.form,user_id)
            jsonarray = json.dumps(outputDataDict)
            return jsonarray

# write user answer
@app.route('/write_answer', methods=['POST'])
def write_answer():
    if request.method == 'POST':
        token=request.form['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        result=WriteAnswer.WriteAnswer(request.form,user_id)
        outputDataDict={"result":result}
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


@app.route('/get_lesson_all_answers', methods=['POST'])
def get_lesson_all_answers():
    if request.method == 'POST':
        token=request.form['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        outputDataDict=GetLessonAllAnswers.GetLessonAllAnswers(request.form,user_id)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


# все авторы языка
@app.route('/get_all_language_autors', methods=['POST'])
def get_all_language_autors():
    if request.method == 'POST':
        token=request.form['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        outputDataDict=GetAllAutorsByLanguage.GetAuotorsByLangugageAndRequestForm(request.form)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


# все модули автора
@app.route('/get_all_autors_modules', methods=['POST'])
def get_all_autors_modules():
    if request.method == 'POST':
        token=request.form['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        outputDataDict=GetAllAutorsModules.GetAllAoutrosModulesByRequstForm(request.form)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


# все уроки модуля
@app.route('/get_all_module_lessons', methods=['POST'])
def get_all_module_lessons():
    if request.method == 'POST':
        token=request.form['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        outputDataDict=GetAllModuleLessons.GetAllModuleLessonsByRequstForm(request.form)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


# все мои модули
@app.route('/get_all_my_modules', methods=['POST'])
def get_all_my_modules():
    if request.method == 'POST':
        token=request.form['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        outputDataDict=GetAllMyModules.GetAllAoutrosModulesByRequstForm(request.form,user_id)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


# добавить мой модуль
@app.route('/add_my_module', methods=['POST'])
def add_my_module():
    if request.method == 'POST':
        token=request.form['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        outputDataDict=AddMyModule.GetAllAoutrosModulesByRequstForm(request.form,user_id)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


#изменить статус модуля
@app.route('/change_module_status', methods=['POST'])
def change_module_status():
    if request.method == 'POST':
        token=request.form['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        outputDataDict=ChangeModuleStatus.ChangeModuleStatus(request.form,user_id)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


#удалить модуль
@app.route('/delete_module', methods=['POST'])
def delete_module():
    if request.method == 'POST':
        token=request.form['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        outputDataDict=DelteModule.DeleteModule(request.form,user_id)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


#добавить урок в модуль
@app.route('/add_lesson_to_module', methods=['POST'])
def add_lesson_to_module():
    if request.method == 'POST':
        token=request.form['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        outputDataDict=AddMyLesson.AddMyLessonByRequstForm(request.form,user_id)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


#изменить статус урока
@app.route('/change_lesson_status', methods=['POST'])
def change_lesson_status():
    if request.method == 'POST':
        token=request.form['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        outputDataDict=ChangeLessonStatus.ChangeLessonStatusByRequestForm(request.form,user_id)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


#удалить урок
@app.route('/delete_lesson', methods=['POST'])
def delete_lesson():
    if request.method == 'POST':
        token=request.form['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        outputDataDict=DeleteLesson.Deletelesson(request.form,user_id)
        jsonarray = json.dumps(outputDataDict)
        return jsonarray


@app.route('/read_lesson', methods=['POST'])
def read_lesson():
    if request.method == 'POST':
        token=request.form['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        if user_id != -1:
         lessonData=ReadLesson.ReadLesson(request.form,user_id)
         jsonarray = json.dumps(lessonData)
         return jsonarray


#записать слово в урок
@app.route('/write_word_to_lesson', methods=['POST'])
def write_word_to_lesson():
    if request.method == 'POST':
        token=request.form['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        if user_id != -1:
            outputDataDict=WriteWordToLesson.WriteWordToLesson(request.form,user_id)
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
#записать список слов в урок

@app.route('/write_word_list_to_lesson', methods=['POST'])
def write_word_list_to_lesson():
    if request.method == 'POST':
        dataDict =  json.loads(request.json)
        for d in dataDict:
            print(d)
        #print(request.form)
        token=dataDict['token']
        user_id = GetUserByToken.GetIdByTocken(token)
        # for r in request.form:
        #     print(r,request.form[r])


        if user_id != -1:
            outputDataDict=WriteWordListToLesson.WriteWordListToLesson(dataDict,user_id)
            jsonarray = json.dumps(outputDataDict)
            return jsonarray


from JSONRequest import CheckAndWriteAnswer
from JSONRequest import WriteWordListToLesson
from JSONRequest import DeleteLesson
from JSONRequest import DelteModule
from JSONRequest import ChangeLessonStatus
from JSONRequest import AddMyLesson
from JSONRequest import WriteWordToLesson
from JSONRequest import ReadLesson
from  JSONRequest import ChangeWordInLesson
from JSONRequest import WriteAnswer
from JSONRequest import GetLessonAllAnswers
from JSONRequest import GetAllAutorsByLanguage
from JSONRequest import GetAllAutorsModules
from JSONRequest import GetAllModuleLessons
from JSONRequest import GetAllMyModules
from JSONRequest import AddMyModule
from JSONRequest import ChangeModuleStatus
from Autorization import GetUserByToken


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run()
