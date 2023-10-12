def get_sum(l1, r1):
    if l1 != 0:
        return sumarr[r1] - sumarr[l1 - 1]
    else:
        return sumarr[r1]


n, m = map(int, input().split())
arr = list(map(int, input().split()))
sumarr = [arr[0]]
for i in range(1, len(arr)):
    sumarr.append(arr[i] + sumarr[i - 1])
while m != 0:
    l, r = map(int, input().split())
    print(get_sum(l - 1, r - 1))
    m -= 1
