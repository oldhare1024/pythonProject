import urllib.request
# url_page='http://www.bilibili.com'
# urllib.request.urlretrieve(url_page,'bilibili.html')
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46'
}
url_img = 'https://xinzhuobu.com/wp-content/uploads/2022/12/20221216003.jpg'
urllib.request.urlretrieve(url=url_img, filename='jk.jpg')
