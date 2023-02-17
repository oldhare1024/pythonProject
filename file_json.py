import json as j

fp = open('demo/test.txt', 'r')
con = fp.read()

re = j.loads(con)
print(re)
fp.close()
