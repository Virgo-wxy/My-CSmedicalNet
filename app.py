# _*_ coding:utf-8 _*_
# 爬取长沙医疗网实时行业快讯
import urllib2
from bs4 import BeautifulSoup
from Demo import work_newsss,db
def get_news(url):
    # url = 'http://www.zhongguoyiliaowang.com/news/class/?99.html'
    response = urllib2.urlopen(url)
    html_text = response.read()
    texts = BeautifulSoup(html_text, 'html.parser')  # 将HTML源代码放入处理源代码的容器中
    title_html1 = texts.find_all("div",class_="newstitle")#新闻原标题
    title_html2 = texts.find_all('div',class_="con")#新闻内容
    title_html3 = texts.find_all('div',class_="info")#新闻发布时间,以及发布者信息
    return title_html1[0].text,title_html2[0],title_html3[0].text

#爬取新闻链接
def get_news_link():
    url = 'http://www.zhongguoyiliaowang.com/news/class/?99.html'
    response = urllib2.urlopen(url)
    html_test = response.read().decode("utf-8")
    texts = BeautifulSoup(html_test, "html.parser")# 将HTML源代码放入处理源代码的容器中
    title_text = texts.find_all("ul", id="queryul")#内容所在位置
    for texts in title_text:
        for text in texts.find_all("a"):
            url1='http://www.zhongguoyiliaowang.com/'+str(text.get("href")[6:])
            news = work_newsss(new_title=get_news(url1)[0],new_concents=str(get_news(url1)[1]),new_info=get_news((url1))[2])
            db.session.add(news)  # 添加回话
            db.session.commit()  # 提交回话
    print '存储成功！'

get_news_link()