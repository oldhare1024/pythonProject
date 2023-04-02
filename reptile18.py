import urllib.request
from lxml import etree
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
}


def create_requst(page):
    if page == 1:
        url = 'http://sc.chinaz.com/tupian/meishitupian.html'
    else:
        url = 'http://sc.chinaz.com/tupian/meishitupian_' + str(page) + '.html'
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@class="container"]//img/@alt')
    src_list = tree.xpath('//div[@class="container"]//img/@data-original')
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'http:' + src
        # print(name, url)
        urllib.request.urlretrieve(url=url, filename='./food/' + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始页'))
    end_page = int(input('请输入终止页'))
    for page in range(start_page, end_page + 1):
        time.sleep(1)
        request = create_requst(page + 1)
        content = get_content(request)
        down_load(content)
