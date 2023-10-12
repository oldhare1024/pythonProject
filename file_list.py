import json

fp = open('demo/test.txt', 'w')
namel = ['lichan', 'yupan', 'xiawenxing']
# n = j.dumps(namel)
# fp.write(n)
json.dump(namel, fp)
fp.close()
