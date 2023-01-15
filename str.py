s1 = "Hello"
print(s1, s1.swapcase(), sep='.', end='\n')  # 大小写互换
print(s1.title())  # 单词首字符变小写
print(s1.capitalize(), )  # 首字符变大写,其余变小写
s2 = " water "
print(s2.strip())  # 去除左右空格
s3 = "www.baidu.com"
print(s3.strip('www.'))  # 删除子串
s4 = input()
s5 = s4.strip('www.')
s4 = s5.strip('.com')
print(s4)
Internet = ['www.', '.com']
s5 = s4.join(Internet)  # 加入间隔子串
print(s5)
s6 = '192.161.1.1'
print(s6.split('.'))  # 去除间隔符
s7 = "1:20"
print(s7.zfill(5))  # 前导0补位
s8 = 'The Witcher:3'
print(s8.replace(' ', '_'))  # 使后者字符替换字符串中前者字符
