import json
import urllib.parse
import urllib.request

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
head = {
    'Cookie': ' APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1676640855,1676697172; BAIDUID=B02DF4155B933605110BDF3D6FD2B24B:FG=1; BAIDUID_BFESS=B02DF4155B933605110BDF3D6FD2B24B:FG=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1676697267',
}
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'iron',
    'simple_means_flag': '3',
    'sign': '760998.1015703',
    'token': '60119f3c910c5097effbead311ed803e',
    'domain': 'common',
}
data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url, data=data, headers=head)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
obj=json.loads(content)
print(obj)
