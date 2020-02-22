#!/usr/bin/python
# -*-  coding:utf-8  -*-

from flask import Flask, render_template, redirect, url_for, request, make_response
from model import get_user_infos, del_user_info, add_user_info, get_work_news, del_work_news, add_work_news, \
    get_product_infos, del_product_info, add_product_info, login_test, get_guestbook, add_guestbooks, \
    manage_get_guestbook, del_guestbook, manage_get_guestbook_answer, add_guestbooks_answer, admin_test, \
    get_hospital_infos, update_work_news, update_product_infos, get_update_product_info
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)


@app.route('/')
def index():
    cookie = request.cookies.get('username')
    if cookie == None:
        cookie = '未登录'
    return render_template('index.html', cookie=cookie)
    # return render_template('index.html')


# 登录的视图函数
@app.route('/login/')
def login():
    cookie = request.cookies.get('username')
    if cookie == None:
        cookie = '未登录'
    return render_template('login.html', cookie=cookie)


# 登录验证
@app.route('/login_test/')
def login_tests():
    user_name = request.values.get('user_name')
    user_password = request.values.get('pwd')
    answer = login_test(user_name, user_password)
    if answer is ():
        titi = '用户名或密码错误！'
        return render_template('login.html', titi=titi)
    else:
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('username', user_name, max_age=300)
        resp.set_cookie('password', user_password, max_age=300)
        return resp


# 注销的视图函数
@app.route('/cancel/')
def cancel():
    resp = make_response(redirect(url_for('index')))
    # 第一种方法
    # resp.set_cookie('username', expires=0)
    # resp.set_cookie('password', expires=0)
    # 第二种方法
    resp.delete_cookie('username')
    resp.delete_cookie('password')
    return resp


# 注册的视图函数
@app.route('/register/')
def register():
    cookie = request.cookies.get('username')
    if cookie == None:
        cookie = '未登录'
    return render_template('register.html', cookie=cookie)


@app.route('/add_user/')
def add_user():
    user_name = request.values.get('user_name')
    user_password = request.values.get('pwd')
    user_email = request.values.get('email')
    add_user_info(user_name, user_password, user_email)
    return render_template('login.html')


# 手机端的视图函数
@app.route('/phone/')
def phone():
    cookie = request.cookies.get('username')
    if cookie == None:
        cookie = '未登录'
    return render_template('phone.html', cookie=cookie)


# 医生的视图函数
@app.route('/doctor/')
def doctor():
    cookie = request.cookies.get('username')
    if cookie == None:
        cookie = '未登录'
    return render_template('doctor.html', cookie=cookie)


# 医院的视图函数
@app.route('/hospital/<page>')
def hospital(page):
    cookie = request.cookies.get('username')
    if cookie == None:
        cookie = '未登录'
    hospital_infos = get_hospital_infos()
    count = hospital_infos.__len__()
    page = int(page)
    if page == 0:
        page = 1
    # 获得总页数
    pages = (count / 6) + 1
    # 获得当前分页所有对象
    cate_data_alls = hospital_infos[page * 6 - 6:page * 6]
    # 上一页的页码
    prev = page - 1
    # 下一页的页码
    if page == pages:
        next = page
    else:
        next = page + 1
    return render_template('hospital.html', cookie=cookie, cate_data_alls=cate_data_alls, pages=pages, prev=prev,
                           next=next, page=page)


# 关于我们的视图函数
@app.route('/company/')
def company():
    cookie = request.cookies.get('username')
    if cookie == None:
        cookie = '未登录'
    return render_template('company.html', cookie=cookie)


# 产品系列的视图函数
@app.route('/product/<page>')
def product(page):
    cookie = request.cookies.get('username')
    if cookie == None:
        cookie = '未登录'
    product_infos = get_product_infos()
    count = product_infos.__len__()
    page = int(page)
    if page == 0:
        page = 1
    # 获得总页数
    pages = (count / 8) + 1
    # 获得当前分页所有对象
    cate_data_alls = product_infos[page * 8 - 8:page * 8]
    # 上一页的页码
    prev = page - 1
    # 下一页的页码
    if page == pages:
        next = page
    else:
        next = page + 1
    return render_template('product.html', cookie=cookie, cate_data_alls=cate_data_alls, pages=pages, prev=prev,
                           next=next, page=page)


# 行业快讯的视图函数
@app.route('/news/<page>')
def news(page):
    cookie = request.cookies.get('username')
    if cookie == None:
        cookie = '未登录'
    work_news = get_work_news()
    count = work_news.__len__()
    page = int(page)
    if page == 0:
        page = 1
    # 获得总页数
    pages = (count / 14) + 1
    # 获得当前分页所有对象
    cate_data_alls = work_news[page * 14 - 14:page * 14]
    # 上一页的页码
    prev = page - 1
    # 下一页的页码
    if page == pages:
        next = page
    else:
        next = page + 1
    return render_template('news.html', cookie=cookie, cate_data_alls=cate_data_alls, pages=pages, prev=prev, next=next,
                           page=page)


@app.route('/work_news/<Cpage>/<news_title>/<news_content>/<news_time>')
def work_news(Cpage, news_title, news_content, news_time):
    cookie = request.cookies.get('username')
    if cookie == None:
        cookie = '未登录'
    return render_template('work_news.html', cookie=cookie, Cpage=Cpage, news_title=news_title,
                           news_content=news_content, news_time=news_time)


# 客户留言的视图函数
@app.route('/guestbook/')
def guestbook():
    cookie = request.cookies.get('username')
    if cookie == None:
        cookie = '未登录'
    guestbook_infos = get_guestbook()
    return render_template('guestbook.html', cookie=cookie, guestbook_infos=guestbook_infos)


@app.route('/add_guestbook/')
def add_guestbook():
    guestbook_name = request.values.get('guestName')
    guestbook_question = request.values.get('guestContent')
    add_guestbooks(guestbook_name, guestbook_question)
    return redirect(url_for('guestbook'))


# 人才招聘的视图函数
@app.route('/recruit/')
def recruit():
    cookie = request.cookies.get('username')
    if cookie == None:
        cookie = '未登录'
    return render_template('recruit.html', cookie=cookie)


# 联系我们的视图函数
@app.route('/contact/')
def contact():
    cookie = request.cookies.get('username')
    if cookie == None:
        cookie = '未登录'
    return render_template('contact.html', cookie=cookie)


# 管理员登录的视图函数
@app.route('/manage/')
def manage():
    return render_template('manage/manage_login.html')


@app.route('/manage_test/')
def manage_test():
    admin_name = request.values.get('admin_name')
    admin_password = request.values.get('pwd')
    answer = admin_test(admin_name, admin_password)
    if answer is ():
        titi = '管理员名或密码错误！'
        return render_template('manage/manage_login.html', titi=titi)
    else:
        return render_template('manage/manage_index.html')


# 后端首页的视图函数
@app.route('/manage_index/')
def manage_index():
    return render_template('manage/manage_index.html')


# 新增用户的视图函数
@app.route('/manage/add_user/')
def manage_add_user():
    return render_template('manage/add_user.html')


@app.route('/manage/add_user_info/')
def add_user_infos():
    user_name = request.values.get('user_name')
    user_password = request.values.get('pwd')
    user_email = request.values.get('email')
    add_user_info(user_name, user_password, user_email)
    return redirect(url_for('manage_add_user'))


# 删除用户的视图函数
@app.route('/manage/user/<page>')
def user(page):
    user_infos = get_user_infos()
    count = user_infos.__len__()
    page = int(page)
    if page == 0:
        page = 1
    # 获得总页数
    pages = (count / 14) + 1
    # 获得当前分页所有对象
    alls = user_infos[page * 14 - 14:page * 14]
    # 上一页的页码
    prev = page - 1
    # 下一页的页码
    if page == pages:
        next = page
    else:
        next = page + 1
    return render_template('manage/del_admin.html', alls=alls, pages=pages, prev=prev, next=next, page=page)


@app.route('/manage/<Cpage>/del_user/<user_name>/<user_email>')
def del_user(Cpage, user_name, user_email):
    del_user_info(user_name, user_email)
    return redirect(url_for('user', page=Cpage))


# 新增产品的视图函数
@app.route('/manage/add_product/')
def manage_product():
    return render_template('manage/add_product.html')


@app.route('/manage/add_product_info/')
def add_product_infos():
    product_name = request.values.get('productName')
    product_image = request.values.get('photo')
    product_image = 'images/product/' + product_image
    product_work = request.values.get('work')
    add_product_info(product_name, product_image, product_work)
    return redirect(url_for('manage_product'))


# 删除产品的视图函数
@app.route('/manage/product/<page>')
def manage_product_show(page):
    product_infos = get_product_infos()
    count = product_infos.__len__()
    page = int(page)
    if page == 0:
        page = 1
    # 获得总页数
    pages = (count / 9) + 1
    # 获得当前分页所有对象
    alls = product_infos[page * 9 - 9:page * 9]
    # 上一页的页码
    prev = page - 1
    # 下一页的页码
    if page == pages:
        next = page
    else:
        next = page + 1
    return render_template('manage/del_product.html', alls=alls, pages=pages, prev=prev, next=next, page=page)


@app.route('/manage/del_product/<Cpage>/<product_name>/<product_work>')
def del_product(Cpage, product_name, product_work):
    del_product_info(product_name, product_work)
    return redirect(url_for('manage_product_show', page=Cpage))


# 修改产品的视图函数
@app.route('/manage/update_product_info/<product_id>')
def update_product_info(product_id):
    infos = get_update_product_info(product_id)
    return render_template('manage/update_product.html', infos=infos)


@app.route('/manage/update_product/')
def update_product():
    product_old_name = request.values.get('old_productName')
    product_name = request.values.get('productName')
    product_image = request.values.get('photo')
    product_image = 'images/product/' + product_image
    product_work = request.values.get('work')
    update_product_infos(product_old_name, product_name, product_image, product_work)
    return redirect(url_for('manage_product_show', page=1))


# 留言回复
@app.route('/manage/guestbook_answer/')
def manage_guestbook_answer_show():
    guestbook_infos = manage_get_guestbook_answer()
    return render_template('manage/guestbook_answer.html', guestbook_infos=guestbook_infos)


@app.route('/manage/add_guestbook_answer/')
def guestbook_answer():
    guestbook_answer = request.values.get('answer')
    guestbook_question = request.values.get('question')
    add_guestbooks_answer(guestbook_answer, guestbook_question)
    return redirect(url_for('manage_guestbook_answer_show'))


# 删除留言的视图函数
@app.route('/manage/guestbook/<page>')
def manage_guestbook_show(page):
    guestbook_infos = manage_get_guestbook()
    count = guestbook_infos.__len__()
    page = int(page)
    if page == 0:
        page = 1
    # 获得总页数
    pages = (count / 14) + 1
    # 获得当前分页所有对象
    alls = guestbook_infos[page * 14 - 14:page * 14]
    # 上一页的页码
    prev = page - 1
    # 下一页的页码
    if page == pages:
        next = page
    else:
        next = page + 1
    return render_template('manage/del_guestbook.html', alls=alls, pages=pages, prev=prev, next=next, page=page)


@app.route('/manage/del_guestbook/<Cpage>/<guestbook_name>/<guestbook_question>')
def manage_del_guestbook(Cpage, guestbook_name, guestbook_question):
    del_guestbook(guestbook_name, guestbook_question)
    return redirect(url_for('manage_guestbook_show', page=Cpage))


# 新增快讯的视图函数
@app.route('/manage/news/')
def manage_news():
    return render_template('manage/add_news.html')


@app.route('/manage/add_news/')
def add_news():
    news_title = request.values.get('title')
    news_content = request.values.get('content')
    add_work_news(news_title, news_content)
    return redirect(url_for('manage_news'))


# 删除快讯的视图函数
@app.route('/manage/work_news/<page>')
def manage_work_news(page):
    work_news = get_work_news()
    count = work_news.__len__()
    page = int(page)
    if page == 0:
        page = 1
    # 获得总页数
    pages = (count / 14) + 1
    # 获得当前分页所有对象
    alls = work_news[page * 14 - 14:page * 14]
    # 上一页的页码
    prev = page - 1
    # 下一页的页码
    if page == pages:
        next = page
    else:
        next = page + 1
    return render_template('manage/del_news.html', alls=alls, pages=pages, prev=prev, next=next, page=page)


@app.route('/manage/del_news/<Cpage>/<news_title>')
def del_news(Cpage, news_title):
    del_work_news(news_title)
    return redirect(url_for('manage_work_news', page=Cpage))


# 修改快讯的视图函数
@app.route('/manage/update_news_info/<news_title>/<news_content>')
def update_news_info(news_title, news_content):
    return render_template('manage/update_news.html', news_title=news_title, news_content=news_content)


@app.route('/manage/update_news/')
def update_news():
    old_title = request.values.get('old_title')
    news_title = request.values.get('title')
    news_content = request.values.get('content')
    update_work_news(old_title, news_title, news_content)
    return redirect(url_for('manage_work_news', page=1))


if __name__ == '__main__':
    app.run(debug=True)
