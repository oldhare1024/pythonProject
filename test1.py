from itertools import permutations


def bubble_sort(s):
    s = list(s)
    n = len(s)
    cnt = 0
    for i in range(n):
        for j in range(n - i - 1):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
                cnt += 1
    return cnt


v = int(input())
ans = None
for length in range(1, 27):
    for s in permutations('abcdefghijklmnopqrstuvwxyz', length):
        if bubble_sort(s) == v:
            if ans is None or len(s) < len(ans) or (len(s) == len(ans) and s < ans):
                ans = ''.join(s)
print(ans)
