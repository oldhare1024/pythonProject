import requests

url = 'http://www.baidu.com/s?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
    'Cookie': 'BIDUPSID=9C67E1A18E34FD5C9B0B30C488F48F62; PSTM=1678774648; BAIDUID=9C67E1A18E34FD5C3E522330FCD86051:FG=1; BD_HOME=1; BD_UPN=12314753; BA_HECTOR=042ga10k2ha0808580ag2l5l1i104bi1m; picUrl=https%3A%2F%2Fdogefs.s3.ladydaily.com%2F~%2Fsource%2Fwallhaven%2Ffull%2F8o%2Fwallhaven-8o2dpj.png%3Fw%3D2560%26fmt%3Dwebp; ZFY=9Sw:BzhR0KBv2ZPxMed65BbG8gAZkY5UzHcMTCZgTF5Y:C; BAIDUID_BFESS=9C67E1A18E34FD5C3E522330FCD86051:FG=1; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=5; H_PS_PSSID=36547_38113_38126_37862_38170_38289_38244_37930_38316_38382_38285_26350_37881; H_PS_645EC=eb191xJNx0Hy98XhIKDs3OAvST37RilKJXAWL3IRq817%2FMisU4xQSXBY2YFk%2FaAzUg',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}
data = {
    'wd': '北京'
}
response = requests.get(url=url, headers=headers, data=data)
response.encoding = 'utf-8'
content = response.text
print(content)
