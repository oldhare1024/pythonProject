# N = input()
# er = 0
# for i in N:
#     if i == '2':
#         er += 1
# if int(N) < 0:
#     digital = len(N) - 1
#     if int(N) % 2 == 0:
#         degree = (er / digital) * 1.5 * 2 * 100
#         print('% .2f%%' % degree)
#     else:
#         degree = (er / digital) * 1.5 * 100
#         print('% .2f%%' % degree)
# elif (int(N)) == 0:
#     print('0.00%')
# else:
#     digital = len(N)
#     degree = (er / digital) * 100
#
#     print('% .2f%%' % degree)
N = input()
er = 0
for i in N:
    if i == '2':
        er += 1
if int(N) < 0:
    digital = len(N) - 1
    if int(N) % 2 == 0:
        degree = (er / digital) * 1.5 * 2 * 100
        print('%.2f%%' % degree)
    else:
        degree = (er / digital) * 1.5 * 100
        print('%.2f%%' % degree)
elif (int(N)) == 0:
    print('0.00%')
else:
    digital = len(N)
    if int(N) % 2 == 0:
        degree = (er / digital) * 2 * 100
        print('%.2f%%' % degree)
    else:
        degree = (er / digital) * 100
        print('%.2f%%' % degree)
