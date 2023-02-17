import urllib.request

url='http://cn.bing.com/?mkt=zh-CN'
response=urllib.request.urlopen(url)
#print(type(response))
content=response.readlines()
#print(content)
print(response.getcode(),end='\n')
print(response.geturl(),end='\n')
print(response.getheaders())
