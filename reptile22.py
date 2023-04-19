# 导入request
# 导入CSV我们到时要保存为csv
import csv
# 导入正规表达，这里是用来让我们的文字更加准确
import re

import requests
# 导入BeautifulSoup
from bs4 import BeautifulSoup

# 我们的个人电脑信息
user_agent = 'Mozilla/5.0(windows NT 10.0;win 64;x64)\AppleWekit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
headers = {'User-Agent': user_agent}
policies = requests.get("http://www.gov.cn/zhengce/zuixin.htm")
# 这里指定我们的编码方式，下次找个机会来讲
policies.encoding = 'utf-8'
# 用这个来解析lxml
p = BeautifulSoup(policies.text, 'lxml')
# 这里是来处理我们爬下里的文本，让他们更加准确
contents = p.find_all(href=re.compile('content'))
# 定义一个空列表
rows = []
# 循环，对每一个链接和标题提取
for content in contents:
    href = content.get('href')
    row = ('国务院', content.string, href)
    rows.append(row)
# 定义CSV的表头
header = ['发文部门', '标题', '链接']
# 建立一个文件，以写入模式打开
with open('policies.csv', 'w', encoding='gb18030') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(header)
    f_csv.writerows(rows)
print('\n\n最新的信息获取完成\n\n')
