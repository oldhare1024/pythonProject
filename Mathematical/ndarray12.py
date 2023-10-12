import numpy as np

a, b = 'hello', 'world'
print('连接{}和{}两个字符串:'.format(a, b))
print(np.char.add([a], [b]))
c, d = 'abc', 'xyz'
print('连接{}和{}两个字符串:'.format(c, d))
print(np.char.add([a, b], [c, d]))
e = 'rabb1t'
print(np.char.multiply(e, 3))
print(np.char.center(e, 20, fillchar='_'))
print(np.char.capitalize(e))
print(np.char.title('i like cat'))
f = 'GTS'
print(np.char.lower([f]))
print(np.char.upper([a, c]))
g = 'www.runoob.com'
print(np.char.split(g, sep='.'))
h = 'i\nlike\rrunoob'
print(np.char.splitlines(h))
i = 'arush b,bro!'
print(np.char.strip(i, 'a'))
print(np.char.join('-', b))
print(np.char.replace(i, 'bro', 'man'))
print(np.char.encode('cp500'))
#print(np.char.decode('&#x72C2;&#x91CE;&#x98D9;&#x8F66;'))
