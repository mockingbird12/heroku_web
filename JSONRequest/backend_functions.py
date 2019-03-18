# -*- coding: utf-8 -*-

from BackendJSON.DatabaseDriver import *

user = Users()
modules = Modules()
lessons = Lessons()
words = Words()
answers = Answers()


def AddMyModule(requestform, user_id):
    error = modules.insert(requestform, user_id)
    if error == '':
        status = 'ok'
    else:
        status = 'error'
    return {"status": status, "error": error}

def DeleteModule(requestform, user_id):
    module_id = requestform['module_id']
    status = 'user '+ str(user_id) + ' delete module ' + str(module_id)
    error = modules.delete(module_id)
    if error != '':
        status = 'error'
    return {"status": status, "error": error}


def ChangeModuleStatus(requestform, user_id):
    show_module = requestform['show_module']
    module_id = requestform['module_id']
    error = modules.update(show_module, module_id)
    status = 'user ' + str(user_id) + ' change:' + str(module_id) + ' status to: ' + str(show_module)
    if error != '':
        status = 'error'
    return {"status": status, "error": error}

def GetAllAutorsModulesByRequestForm(user_id):
    return (modules.select_by_user(user_id))

def GetAllModuleLessonsByRequestForm(requestform):
    module_id = requestform['module_id']
    return (lessons.select_by_module(module_id))

def AddMyLessonByRequestForm(requestform, user_id):
    module_id = requestform['module_id']
    lesson_name = requestform['lesson']
    show_lesson = requestform['show_lesson']
    status = 'user_id ' + str(user_id) + ' ,add ' + str(lesson_name) + ' in module ' + str(module_id) + ' ,status: ' + str(show_lesson)
    error = lessons.insert(requestform)
    if error != '':
        status = 'error'
    return {"status": status, "error": error}

def ReadLesson(requestform):
    lesson_id = requestform['lesson_id']
    return lessons.select_by_id(lesson_id)

def ChangeLessonStatusByRequestForm(requestform, user_id):
    lesson_id = requestform['lesson_id']
    show_lesson = requestform['show_lesson']
    module = requestform['module_id']
    status = 'user ' + str(user_id) + ' change: ' + str(module) + ' ,lesson ' + str(lesson_id) + ' status to: ' + str(show_lesson)
    error = ''
    try:
        lessons.update(show_lesson, lesson_id)
    except Exception as err:
        status = 'error'
        error = str(err)
    return {"status": status, "error": error}


def DeleteLesson(requestform, user_id):
    lesson_id = requestform['lesson_id']
    module = requestform['module_id']
    error = ''
    status = 'user ' + str(user_id) + ' delete lesson ' + str(lesson_id) + ' from module ' + str(module)
    try:
        lessons.delete(lesson_id)
    except Exception as err:
        status = 'error'
        error = str(err)
    return {"status": status, "error": error}


def WriteWordToLesson(requestform, user_id):
    lesson_id = requestform['lesson_id']
    word = requestform['word']
    translate = requestform['translate']
    comment = requestform['comment']
    words.insert(requestform)


def WriteWordListToLesson(requestform, user_id):
    word_list = requestform['word_list']
    word_dict = {}
    error = ''
    status = ''
    for w in word_list:
        word_dict.update({'lesson_id': requestform['lesson_id']})
        word_dict.update({'word': w['word']})
        word_dict.update({'translate': w['translate']})
        word_dict.update({'word_comment': w['comment']})
        try:
            words.insert(word_dict)
        except Exception as err:
            status = 'error'
            error = str(err)
        return {"status": status, "error": error}


def ChangeWordInLesson(requestform):
    status = words.update(requestform)
    return status

def CheckAndWriteAnswer(requestform):
    word_id = requestform['word_id']
    answers_user = requestform['answer'] #from user
    error = answers.insert(requestform)
    status = ''
    right_answer = 'no'
    if requestform['translate'] == requestform['answer']:
        right_answer = 'yes'
    status = 'user: ' + str(requestform['user_id']) + ' write word_id: ' + str(requestform['word_id']) + ' answer: '\
             + right_answer + ' error:' + error
    return status



def GetLessonAllAnswers(requestform, user_id):
    lesson_id = requestform['lesson_id']
    return answers.read_by_lesson(lesson_id)

def GetAutorsByLanguageAndRequestForm(requestform):
    language_from = requestform['language_from']
    language_to = requestform['language_to']
    return modules.select_by_language(language_from, language_to)