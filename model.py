#!/usr/bin/python
# -*-  coding:utf-8  -*-

import pymysql as db
import json


def get_user_infos():
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        sql = "SELECT * FROM user_infos"
        cursor.execute(sql)
        user_infos = cursor.fetchall()
        return user_infos
    except Exception as e:
        print(e)
        print '数据库操作失败！'
    finally:
        cursor.close()
        conn.close()


def del_user_info(user_name, user_email):
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        user_name = str(user_name)
        user_email = str(user_email)
        sql = "delete FROM user_infos where user_name='%s' and user_email='%s'" % (user_name, user_email)
        rownum = cursor.execute(sql)
        conn.commit()
        return rownum
    except Exception as e:
        print(e)
        print '数据库操作失败！'
    finally:
        cursor.close()
        conn.close()


def add_user_info(user_name, user_password, user_email):
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        sql = "INSERT INTO user_infos(user_name,user_password,user_email) VALUES ('%s','%s','%s')" % (
        user_name, user_password, user_email)
        rownum = cursor.execute(sql)
        conn.commit()
        return rownum
    except Exception as e:
        print(e)
        print("数据库操作失败")
    finally:
        cursor.close()
        conn.close()


def get_work_news():
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        sql = "SELECT * FROM work_news"
        cursor.execute(sql)
        work_news = cursor.fetchall()
        return work_news
    except Exception as e:
        print(e)
        print '数据库操作失败！'
    finally:
        cursor.close()
        conn.close()


def del_work_news(news_title):
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        news_title = str(news_title)
        sql = "delete FROM work_news where news_title='%s'" % news_title
        rownum = cursor.execute(sql)
        conn.commit()
        return rownum
    except Exception as e:
        print(e)
        print '数据库操作失败！'
    finally:
        cursor.close()
        conn.close()


def update_work_news(old_title, news_title, news_content):
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        old_title = str(old_title)
        news_title = str(news_title)
        news_content = str(news_content)
        sql = "update work_news set news_title = '%s',news_content = '%s' where news_title = '%s'" % (
        news_title, news_content, old_title)
        rownum = cursor.execute(sql)
        conn.commit()
        return rownum
    except Exception as e:
        print(e)
        print '数据库操作失败！'
    finally:
        cursor.close()
        conn.close()


def add_work_news(news_title, news_content):
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        sql = "INSERT INTO work_news(news_title, news_content) VALUES ('%s','%s')" % (news_title, news_content)
        rownum = cursor.execute(sql)
        conn.commit()
        return rownum
    except Exception as e:
        print(e)
        print("数据库操作失败")
    finally:
        cursor.close()
        conn.close()


def get_product_infos():
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        sql = "SELECT * FROM product_infos"
        cursor.execute(sql)
        product_infos = cursor.fetchall()
        return product_infos
    except Exception as e:
        print(e)
        print '数据库操作失败！'
    finally:
        cursor.close()
        conn.close()


def del_product_info(product_name, product_work):
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        product_name = str(product_name)
        product_work = str(product_work)
        sql = "delete FROM product_infos where product_name='%s' and product_work='%s'" % (product_name, product_work)
        rownum = cursor.execute(sql)
        conn.commit()
        return rownum
    except Exception as e:
        print(e)
        print '数据库操作失败！'
    finally:
        cursor.close()
        conn.close()


def get_update_product_info(product_id):
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        product_id = int(product_id)
        sql = "SELECT * FROM product_infos where product_id = '%d'" % product_id
        cursor.execute(sql)
        product_infos = cursor.fetchall()
        return product_infos
    except Exception as e:
        print(e)
        print '数据库操作失败！'
    finally:
        cursor.close()
        conn.close()


def update_product_infos(product_old_name, product_name, product_image, product_work):
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        product_old_name = str(product_old_name)
        product_name = str(product_name)
        product_image = str(product_image)
        product_work = str(product_work)
        sql = "update product_infos set product_name = '%s',product_image = '%s',product_work = '%s' where product_name = '%s'" % (
        product_name, product_image, product_work, product_old_name)
        rownum = cursor.execute(sql)
        conn.commit()
        return rownum
    except Exception as e:
        print(e)
        print '数据库操作失败！'
    finally:
        cursor.close()
        conn.close()


def add_product_info(product_name, product_image, product_work):
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        sql = "INSERT INTO product_infos(product_name, product_image, product_work) VALUES ('%s','%s','%s')" % (
        product_name, product_image, product_work)
        rownum = cursor.execute(sql)
        conn.commit()
        return rownum
    except Exception as e:
        print(e)
        print("数据库操作失败")
    finally:
        cursor.close()
        conn.close()


def login_test(user_name, user_password):
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        user_name = str(user_name)
        user_password = str(user_password)
        sql = "SELECT * FROM user_infos where user_name='%s' and user_password='%s'" % (user_name, user_password)
        cursor.execute(sql)
        test = cursor.fetchall()
        return test
    except Exception as e:
        print(e)
        print '数据库操作失败！'
    finally:
        cursor.close()
        conn.close()


def get_guestbook():
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        sql = "SELECT * FROM guestbook where guestbook_answer != '' order by guestbook_id DESC"
        cursor.execute(sql)
        guestbook_infos = cursor.fetchall()
        return guestbook_infos
    except Exception as e:
        print(e)
        print '数据库操作失败！'
    finally:
        cursor.close()
        conn.close()


def add_guestbooks(guestbook_name, guestbook_question):
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        sql = "INSERT INTO guestbook(guestbook_name, guestbook_question) VALUES ('%s','%s')" % (
        guestbook_name, guestbook_question)
        rownum = cursor.execute(sql)
        conn.commit()
        return rownum
    except Exception as e:
        print(e)
        print("数据库操作失败")
    finally:
        cursor.close()
        conn.close()


def manage_get_guestbook():
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        sql = "SELECT * FROM guestbook"
        cursor.execute(sql)
        guestbook_infos = cursor.fetchall()
        return guestbook_infos
    except Exception as e:
        print(e)
        print '数据库操作失败！'
    finally:
        cursor.close()
        conn.close()


def del_guestbook(guestbook_name, guestbook_question):
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        guestbook_name = str(guestbook_name)
        guestbook_question = str(guestbook_question)
        sql = "delete FROM guestbook where guestbook_name='%s' and guestbook_question='%s'" % (
        guestbook_name, guestbook_question)
        rownum = cursor.execute(sql)
        conn.commit()
        return rownum
    except Exception as e:
        print(e)
        print '数据库操作失败！'
    finally:
        cursor.close()
        conn.close()


def manage_get_guestbook_answer():
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        sql = "SELECT * FROM guestbook where guestbook_answer is Null"
        cursor.execute(sql)
        guestbook_infos = cursor.fetchall()
        return guestbook_infos
    except Exception as e:
        print(e)
        print '数据库操作失败！'
    finally:
        cursor.close()
        conn.close()


def add_guestbooks_answer(guestbook_answer, guestbook_question):
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        guestbook_answer = str(guestbook_answer)
        guestbook_question = str(guestbook_question)
        sql = "update guestbook set guestbook_answer = '%s' where guestbook_question = '%s'" % (
        guestbook_answer, guestbook_question)
        rownum = cursor.execute(sql)
        conn.commit()
        return rownum
    except Exception as e:
        print(e)
        print("数据库操作失败")
    finally:
        cursor.close()
        conn.close()


def admin_test(admin_name, admin_password):
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        admin_name = str(admin_name)
        admin_password = str(admin_password)
        sql = "SELECT * FROM admin_infos where admin_name='%s' and admin_password='%s'" % (admin_name, admin_password)
        cursor.execute(sql)
        test = cursor.fetchall()
        return test
    except Exception as e:
        print(e)
        print '数据库操作失败！'
    finally:
        cursor.close()
        conn.close()


def get_hospital_infos():
    try:
        conn = db.Connect('127.0.0.1', 'root', 'root', 'csmedicalnet', charset='utf8')
        cursor = conn.cursor()
        sql = "SELECT * FROM hospital"
        cursor.execute(sql)
        hospital_infos = cursor.fetchall()
        return hospital_infos
    except Exception as e:
        print(e)
        print '数据库操作失败！'
    finally:
        cursor.close()
        conn.close()
