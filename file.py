# open('test.txt','w')
fp = open('demo/test.txt', 'r')
# for i in range(5):
#     fp.write('hello\n' * 2)
content = fp.readlines()
print(content)
fp.close()
