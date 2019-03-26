# -*- coding: utf-8 -*-

import psycopg2
import time
import os

class DBdriver():
    # conn = psycopg2.connect("host='localhost' dbname='testdb' user='pythonspot' password='111111'")
    conn = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')
    conn.set_client_encoding('UTF8')
    cur = conn.cursor()
    table_name = None

    def read_all(self):
        sql = "SELECT * FROM %s" % self.table_name
        self.cur.execute(sql)
        print(self.table_name)
        for i in self.cur.fetchall():
            print(i)

    def _select(self, sql, data):
        self.cur.execute(sql, data)
        return [i for i in self.cur.fetchall()]

    def rollback(self):
        self.conn.rollback()

    def delete(self, id):
        sql = "DELETE FROM " + self.table_name + " CASCADE WHERE id=" + str(id)
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as err:
            self.rollback()
            return str(err)
        return ''

    def _insert(self, sql, data):
        try:
            self.cur.execute(sql, data)
            self.conn.commit()
        except Exception as err:
            self.rollback()
            return str(err)
        return ''

    def _update(self, sql, data):
        try:
            self.cur.execute(sql, data)
            self.conn.commit()
        except Exception as err:
            self.rollback()
            return str(err)
        return ''


class Users(DBdriver):
    table_name = 'users'

    def __init__(self):
        sql = "CREATE TABLE IF NOT EXISTS "+self.table_name+"(id SERIAL PRIMARY KEY, login VARCHAR(20) UNIQUE, passwd VARCHAR(20)," \
              " token VARCHAR(20), status VARCHAR(20))"
        self.cur.execute(sql)
        self.conn.commit()

    def insert(self, data):
        sql = "INSERT INTO users (login, passwd, token, status) VALUES(%s, %s, %s, %s)"
        data = (data.get('login'), data.get('passwd'), data.get('token'), data.get('status'))
        return super()._insert(sql, data)


class Modules(DBdriver):
    table_name = 'modules'

    def __init__(self):
        sql = "CREATE TABLE IF NOT EXISTS "+self.table_name+"(id SERIAL PRIMARY KEY, user_id INTEGER, language_from VARCHAR(20)," \
            " language_to VARCHAR(20), module VARCHAR(20) UNIQUE, show_module BOOLEAN, module_comment TEXT, " \
                                                            "FOREIGN KEY (user_id) REFERENCES users(id))"
        self.cur.execute(sql)
        self.conn.commit()

    def insert(self, requestform, user_id):
        sql = "INSERT INTO modules(user_id, language_from, language_to, module, show_module, module_comment)" \
            "VALUES (%s, %s, %s, %s, %s, %s)"
        data = (user_id, requestform.get('language_from'), requestform.get('language_to'), requestform.get('module'), \
                requestform.get('show_module'), requestform.get('module_comment'))
        return super()._insert(sql, data)

    def update(self, status, module_id):
        sql = "UPDATE modules SET show_module = %s WHERE id = %s"
        data = (status, module_id)
        return super()._update(sql, data)


    def select_by_user(self, user_id):
        if user_id:
            sql = "SELECT * FROM modules WHERE user_id = %s"
            data = (user_id,)
            res = super()._select(sql, data)
            return res
        else:
            return 'Error user_id is empty'

    def select_by_language(self, language_from, language_to):
        sql = "SELECT * FROM modules WHERE language_from = %s AND language_to = %s"
        data = (language_from, language_to)
        res = super()._select(sql, data)
        return res

class Lessons(DBdriver):
    table_name = 'lessons'

    def __init__(self):
        sql = "CREATE TABLE IF NOT EXISTS "+self.table_name+"(id SERIAL PRIMARY KEY, module_id INTEGER REFERENCES modules" \
            " ON DELETE CASCADE, lesson VARCHAR(20) UNIQUE," \
            " show_lesson BOOLEAN, lesson_comment TEXT, FOREIGN KEY (module_id) REFERENCES modules (id))"
        self.cur.execute(sql)
        self.conn.commit()

    def insert(self, formdata):
        sql = "INSERT INTO lessons(module_id, lesson, show_lesson, lesson_comment) VALUES (%s, %s, %s, %s)"
        data = (formdata.get('module_id'), formdata.get('lesson'), formdata.get('show_lesson'), formdata.get('lesson_comment'))
        return super()._insert(sql, data)

    def select_by_module(self, module_id):
        sql = "SELECT * FROM lessons WHERE module_id = %s"
        data = (module_id,)
        return super()._select(sql, data)

    def update(self, status, lesson_id):
        sql = "UPDATE lessons SET show_lesson = %s WHERE id = %s"
        data = (status, lesson_id)
        return super()._update(sql, data)


class Words(DBdriver):
    table_name = 'words'

    def __init__(self):
        sql = "CREATE TABLE IF NOT EXISTS words(id SERIAL PRIMARY KEY, lesson_id INTEGER, word VARCHAR(20)," \
              " translate VARCHAR(20), word_comment TEXT, FOREIGN KEY (lesson_id) REFERENCES lessons (id))"
        self.cur.execute(sql)
        self.conn.commit()

    def insert(self, data):
        sql = "INSERT INTO words(lesson_id, word, translate, word_comment) VALUES (%s, %s, %s, %s)"
        sql_data = (data.get('lesson_id'), data.get('word'), data.get('translate'), data.get('word_comment'))
        print(sql)
        return super()._insert(sql, sql_data)

    def update(self, data):
        sql = "UPDATE words SET word = %s, translate = %s WHERE id = %s"
        sql_data = (data['word'], data['translate'], data['id'])
        return super()._update(sql, sql_data)

    def select_by_lesson(self, lesson_id):
        sql = "SELECT * FROM words WHERE lesson_id = %s"
        data = (lesson_id,)
        return super()._select(sql, data)


class Answers(DBdriver):
    table_name = 'answers'

    def __init__(self):
        sql = "CREATE TABLE IF NOT EXISTS answers(id SERIAL PRIMARY KEY, user_id INTEGER, lesson_id INTEGER, word_id INTEGER," \
              "answer VARCHAR(20), date DATE, FOREIGN KEY (user_id) REFERENCES users (id))"
        self.cur.execute(sql)
        self.conn.commit()

    def insert(self, data):
        sql = "INSERT INTO answers(user_id, lesson_id, word_id, answer, date) VALUES (%s, %s, %s, %s, %s)"
        data =  (data.get('user_id'), data.get('lesson_id'), data.get('word_id'), data.get('answer'), time.asctime())
        return super()._insert(sql, data)

    def read_by_lesson(self, lesson_id):
        sql = "SELECT * FROM answers WHERE lesson_id = %s"
        data = (lesson_id,)
        return super()._select(sql, data)
