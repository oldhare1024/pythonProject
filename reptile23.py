# 在上述程序中，crawl()函数通过requests库抓取指定网页的HTML
# 代码，并使用BeautifulSoup库解析HTML，提取出页面的标题、摘要和链接。save()函数将提取出的内容存储到SQLite数据库中。search()函数则从数据库中检索出与关键字匹配的内容并返回。
# 在运行程序之前，需要先安装requests、beautifulsoup4和sqlite3库，以及下载对应的WebDriver（如ChromeDriver）并添加到系统PATH中。程序运行后，会在当前目录下创建一个名为search.db的SQLite
# 数据库文件，用于存储网页内容。用户输入关键字时，程序会检索数据库并返回与关键字匹配的页面标题、摘要和链接等信息。
# 需要注意的是，为了遵守网络爬虫的规范，程序应该设置适当的抓取频率、使用User - Agent伪装成浏览器、避免频繁抓取同一页面等，以防止对被抓取网站造成不必要的负担和影响。
import requests
import sqlite3
from bs4 import BeautifulSoup


# 抓取网页信息并提取内容
def crawl(url,content):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    summary = soup.find('meta', attrs={'name': 'description'}).get('content')
    return title, summary, url


# 存储内容到数据库
def save(title, summary, url):
    conn = sqlite3.connect('search.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS pages (title TEXT, summary TEXT, url TEXT)')
    cursor.execute('INSERT INTO pages (title, summary, url) VALUES (?, ?, ?)', (title, summary, url))
    conn.commit()
    conn.close()


# 搜索关键字并返回结果
def search(keyword):
    conn = sqlite3.connect('search.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pages WHERE title LIKE ? OR summary LIKE ?', ('%' + keyword + '%', '%' + keyword + '%'))
    results = cursor.fetchall()
    conn.close()
    return results


# 测试程序
url = 'http://www.baidu.com/'
title, summary, url = crawl(url,content)
save(title, summary, url)
results = search('高考')
print(results)
