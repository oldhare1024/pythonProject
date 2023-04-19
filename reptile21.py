import webbrowser
from urllib.parse import quote

import easygui


def search_url(str1, str2, str3, str4):
    burl = 'http://sousuo.gov.cn/s.htm?t=zhengcelibrary&q=' + str1 + '&timetype=' + str2 + '&mintime=&maxtime=&sort=' + str3 + '&sortType=1&searchfield=' + str4 + '&pcodeJiguan=&bmfl=&childtype=&subchildtype=&tsbq=&pubtimeyear=&puborg=&pcodeYear=&pcodeNum=&filetype=&p=0&n=5&orpro=&inpro='
    return burl


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}


# data = {
#     'q': '',
#     't': 'zhengcelibrary',
#     'orpro': ''
# }


def search_key():
    print("请输入搜索关键词：")
    str1 = input()
    # data["q"] = str1
    str1 = quote(str1)
    return str1


def search_time():
    print('请输入筛选方式：一周内/一月内/一年内/不限')
    timetype = input()
    if timetype == '一年内':
        str2 = 'timeyn'
    elif timetype == '一月内':
        str2 = 'timeyy'
    elif timetype == '一周内':
        str2 = 'timeyz'
    else:
        str2 = 'timeqb'
    return str2


def search_sort():
    print("请输入搜索结果排序方式：按相关度/按时间")
    str3 = input()
    if str3 == "按时间":
        str3 = 'pubtime'
    else:
        str3 = 'score'
    return str3


def search_site():
    print('请输入搜索位置：全文/标题')
    str4 = input()
    if str4 == '标题':
        str4 = 'title'
    elif str4 == '全文':
        str4 = ''
    return str4


def search_down(content):
    f = open('D:/policy.html', 'w', encoding='utf-8')  # 打开一个文件，没有就新建一个
    f.write(content)
    f.close()
    webbrowser.open_new_tab('D:/policy.html')


def search_gui():
    key=easygui.enterbox('请在下框中输入关键词','政策智能检索系统')

if __name__ == '__main__':
    search_gui()
    # s1 = search_key()
    # s2 = search_time()
    # s3 = search_sort()
    # s4 = search_site()
    # url = search_url(s1, s2, s3, s4)
    # requests = urllib.request.Request(url=url, headers=header)
    # response = urllib.request.urlopen(requests)
    # content = response.read().decode('utf-8')
    # search_down(content)
