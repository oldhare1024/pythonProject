import urllib.request

url='http://www.baidu.com/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
}
requests=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(requests)
content=response.read().decode('utf-8')
from lxml import etree
tree=etree.HTML(content)
result=tree.xpath('//input[@id="su"]/@value')[0]
print(result)