import urllib.request

head={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46'
}
url='https://www.baidu.com/s?wd='
name=urllib.parse.quote('周杰伦')
print(url+name)

request=urllib.request.Request(url=url,headers=head)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
#print(content)