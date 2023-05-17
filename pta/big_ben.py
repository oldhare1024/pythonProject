# hh, mm = map(int, input().split(':'))
hh, mm = input().split(':')
dang = 0
if int(hh) in range(0, 12):
    print(f'Only {hh}:{mm}.  Too early to Dang.')
elif int(hh) == 12:
    if int(mm) == 0:
        print(f'Only {hh}:{mm}.  Too early to Dang.')
    else:
        print('Dang')
else:
    dang = int(hh) - 12
    if int(mm) != 0:
        dang += 1
    print('Dang' * dang)
