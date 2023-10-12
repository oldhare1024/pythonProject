import pandas as pd

# df=pd.read_csv('nba.csv')
# #print(df.to_string())
# nm = ["Google", "Runoob", "Taobao", "Wiki"]
# st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
# ag = [90, 40, 80, 98]
#
# dict={'name':nm,'site':st,'age':ag}
# df2=pd.DataFrame(dict)
# df2.to_csv('sites.csv')
# df=pd.read_csv('nba.csv')
# print(df.head(7))
# print(df.tail(5))
# print(df.info())
URL = 'https://static.runoob.com/download/sites.json'
df2 = pd.read_json(URL)
print(df2)
