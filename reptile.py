import urllib.request

url = 'http://cn.bing.com/?mkt=zh-CN'
response = urllib.request.urlopen(url)
content = response.read().decode('UTF-8')
print(content)
