# _*_ coding:utf-8 _*_
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(config)
#存储标题的数据库
class work_news(db.Model):
    __tablename__ = "work_news"
    new_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    new_title = db.Column(db.Text)
    new_concents = db.Column(db.Text)
    new_info = db.Column(db.Text)
db.create_all()
#存储时间的数据库
# class work_news_times(db.Model):
#     __tablename__ = "work_news_TIMES"
#     new_works_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
#     new_works_time = db.Column(db.Text)
# #存储内容的数据库
# class work_news_concents(db.Model):
#     __tablename__ = "work_news_concents"
#     contents_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
#     contents_news = db.Column(db.Text)
