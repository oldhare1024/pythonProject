import urllib.request

url = 'http://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
    'cookie': 'BAIDUID=3AC611A3116850A15948615596C0F2EF:FG=1; BAIDUID_BFESS=3AC611A3116850A15948615596C0F2EF:FG=1; BIDUPSID=3AC611A3116850A15948615596C0F2EF; PSTM=1678358594; BD_HOME=1; H_PS_PSSID=36552_38171_38289_37929_38314_38323_26350_37881; BD_UPN=12314753; BA_HECTOR=000h0k20a081al2ga5ah8g3k1i0je221n; picUrl=https%3A%2F%2Fdogefs.s3.ladydaily.com%2F~%2Fsource%2Fwallhaven%2Ffull%2F8o%2Fwallhaven-8o2dpj.png%3Fw%3D2560%26fmt%3Dwebp; ZFY=oFvI0bsuq5ReyOBp7qIPLzJPNhDSbF:AqA2N927sMAeM:C; delPer=0; BD_CK_SAM=1; PSINO=3; H_PS_645EC=6565MG3WoCKN1EKRXwxDK6oi5TYfqWuUJPMJk%2FX36QUUVEH3iVBKp%2FLr7Ic; baikeVisitId=3cf2559b-fea8-4af2-a558-bb126651f132; B64_BOT=1; COOKIE_SESSION=9700824_0_7_2_7_4_1_0_6_4_0_1_444_0_0_0_1664803454_0_1678358609%7C9%230_0_1678358609%7C1'
}
request = urllib.request.Request(url=url, headers=headers)
# response=urllib.request.urlopen(request)
proxies = {
    'http': '112.14.47.6:52024',
}
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')
with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
response.close()
