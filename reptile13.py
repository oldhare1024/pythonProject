import urllib.request

url = 'https://weibo.cn/7765033060/info'
headers = {
    'accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': ' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': ' max-age=0',
    'cookie': ' _T_WM=77876883397; SSOLoginState=1678335817; ALF=1680927817; SUB=_2A25JDS8ZDeRhGeFJ7VcR8y3MzTyIHXVq8bFRrDV6PUNbktANLRLYkW1Nf36eiaGr5PWCODX16aAdD1C2WfdKxbM5; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFp83FsGW_vWIx.JgG1UwLh5JpX5KzhUgL.FoMNSo-7e0e7So52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0qfehe0ehq7',
    'referer': ' https://weibo.cn/?sudaref=security.weibo.com&luicode=10000011&lfid=231583&rand=1068&p=r',
    'sec-ch-ua': ' "Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': ' ?0',
    'sec-ch-ua-platform': ' "Windows"',
    'sec-fetch-dest': ' document',
    'sec-fetch-mode': ' navigate',
    'sec-fetch-site': ' same-origin',
    'sec-fetch-user': ' ?1',
    'upgrade-insecure-requests': ' 1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
}
requests = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(requests)
content = response.read().decode('utf-8')
with open('weibo.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
