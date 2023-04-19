import os
import re

import requests

global i
name = input("请输入想下载其图片的人物姓名")
path = 'D:/'
if not os.path.exists(name):
    os.mkdir(path + name)
page = int(input("请输入想要的图片页数(一页30张)："))
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46',
    'cookie': "indexPageSugList=%5B%22lisa%22%2C%22%E8%83%A1%E6%AD%8C%22%5D; BIDUPSID=\
    5DCC67F943E17116DE33CB4DA1740216; \
    BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; BAIDUID=5DCC67F943E1711616F95733A6A1E2AA:FG=1; userFrom=cn.bing.com; \
    BAIDUID_BFESS=5DCC67F943E1711616F95733A6A1E2AA:FG=1; firstShowTip=1; \
    BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm",
}
urls = ['https://image.baidu.com/search/index?tn=\
baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=\
0&istype=2&ie=utf-8&fm=index&pos=history&word='
        + name + '&pn={}'.format(i) for i in range(30, page * 30 + 1, 30)
        ]


def get_img(url1):
    response = requests.get(url=url1, headers=head)
    content = response.content.decode('utf-8')
    img_urls = re.findall('"thumbURL":"(.*?)"', content, re.S)
    global i
    i = 1
    for img_urls in img_urls:
        response = requests.get(img_urls, headers=head)
        content = response.content
        with open(path + name + '/{}.jpg'.format(i), 'wb') as f:
            f.write(content)
            print(f'正在为你爬取第{i}张图片\n')
        i += 1


if __name__ == '__main__':
    print(f'开始下载{name}的照片...\n')
for url in urls:
    get_img(url)
print(f'下载已完成,一共{i}张图片保存在D盘{name}文件夹中')
input()
input()
