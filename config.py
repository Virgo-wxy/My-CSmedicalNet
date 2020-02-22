# _*_ coding:utf-8 _*_
DIVBUG = True
# 数据库名称
DIALECT = "mysql"
# 数据库连接驱动
DRIVER = 'pymysql'
# 数据库用户名
USERNAME = "root"
# 数据库密码
PASSWORD = "root"
# 主机地址
HOST = '127.0.0.1'
# 端口号
PORT = '3306'
# 连接数据库名称
DATABASE = 'csmedicalnet'
# flask-sqlalchemy数据URL资源地址，类似
# mysql+pymysql://root:ROOT@localhost:3306/asksystem?charset=utf8
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
)
# 是否跟踪修改，一般为false
SQLALCHEMY_TRACK_MODIFICATIONS = False

# # 每页数量
# FLASKY_POSTS_PER
# 加密标志
# SECRET_KEY = 'PENGZHEN'
