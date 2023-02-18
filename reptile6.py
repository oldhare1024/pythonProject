import json
import urllib.parse
import urllib.request

base_url = 'https://fanyi.baidu.com/sug'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46'
}
data = {
    'kw': 'spider'
}
data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=base_url, data=data, headers=head)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
obj=json.loads(content)
print(obj)

