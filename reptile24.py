# encoding:utf-8
import re
import urllib.parse
import urllib.request

i = 0
# url='http://store.steampowered.com/search/?sort_by=&sort_order=0&category1=998%2C996&special_categories=&filter=topsellers&page=1'
url = 'http://store.steampowered.com/games/#tab=TopSellers'
#    url='http://store.steampowered.com/search/?sort_by=&sort_order=0&category1=998%2C996&special_categories=&filter=topsellers&page='+str(i)
request = urllib.request(url)
response = urllib.request.urlopen(request)
data = response.read()
reg = r'discount_final_price">(¥ \d+).+?\n.+?<div class="tab_item_name">([^<]*)</div>.+?\n.+?\n.+?' + \
      r'<div class="tab_item_top_tags">(?:<span class="top_tag">(.+?)</span>)</div>'
#    r'(<span class="top_tag">.+?</span>){3}'
imgre = re.compile(reg)
imglist = re.findall(imgre, data)
print(imglist)

for pro in imglist:
    print(pro[:-1])
    tag = str(pro[2]).split('</span><span class="top_tag">, ')
    print(tag)
