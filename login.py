import requests

url = 'http://10.1.99.100:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C0%2C20212344051&user_password=182713&wlan_user_ip=10.2.120.64&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=10.1.1.1&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=8405&lang=zh'

data = {
    'callback': 'dr1003',
    'login_method': ' 1',
    'user_account': ',0,20212344051',
    'user_password': '182713',
    'wlan_user_ip': '10.2.120.64',
    'wlan_user_ipv6': '',
    'wlan_user_mac': '000000000000',
    'wlan_ac_ip': '10.1.1.1',
    'wlan_ac_name': '',
    'jsVersion': '4.1.3',
    'terminal_type': '1',
    'lang': 'zh-cn',
    'v': '8405',
}
header = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Host': '10.1.99.100:801',
    'Referer': 'http://10.1.99.100/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
}
# fr = open('D:\login.txt')  # 打开文件
# res = fr.read()  # 读取文件的所有内容，类型为string
# fr.close()
# user_list = res.split()  # 默认以空格或者换行符分隔字符串，返回值为list
# data['user_account'] = user_list[0]
# data['user_password'] = user_list[1]
response = requests.post(url=url, data=data, headers=header).status_code
print("{}".format(response))
