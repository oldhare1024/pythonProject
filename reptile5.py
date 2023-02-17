import urllib.request
import urllib.parse

data = {
    'wd': '周冬雨',
    'sex': '女',
    'location': '中国'
}
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46'
}
a = 'https://www.baidu.com/s?'
b = urllib.parse.urlencode(data)
url = a + b
print(url)
request = urllib.request.Request(url=url, headers=head)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
#print(content)
