import urllib.error
import urllib.parse
import urllib.request


def create_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cookie': 'route-cell=ksa; ASP.NET_SessionId=ajlyjk52cmlrvvynvk3k2crp; SERVERID=6b677b5b776e491db687ec71251cfda0|1678328598|1678327632',
        'cname': '无锡',
        'pid': ' ',
        'pageIndex': page,
        'pageSize': '10'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
    }
    requests = urllib.request.Request(url=base_url, data=data, headers=headers)
    return requests


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(page, content):
    with open('kfc_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    try:
        start_page = int(input('请输入起始页'))
        end_page = int(input('请输入结束页'))

        for page in range(start_page, end_page + 1):
            request = create_request(page)
            content = get_content(request)
            down_load(page, content)
    except urllib.error.HTTPError:
        print('你的网络出现错误')
    except urllib.error.URLError:
        print('都是你的原因，与本作者无关')
