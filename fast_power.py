# a, b, c = map(int, input().split())
# ans = 1
# a %= c
# while b:
#     if b % 2 == 1:
#         ans = ans * a % c
#     a = a * a % c
#     b /= 2
# print(ans)
n, k = map(int, input().split())
c = pow(10, 9) + 7
n %= c
ans = 1
while k != 0:
    if k % 2 == 1:
        ans = ans * n % c
    n = n ** 2 % c
    k //= 2
print(ans)
