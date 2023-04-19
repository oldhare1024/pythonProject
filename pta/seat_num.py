i = j = k = 0
N = int(input())
Id = [0] * N
Seat_num1 = [0] * N
Seat_num2 = [0] * N
for i in range(N):
    Id[i], Seat_num1[i], Seat_num2[i] = map(int, input().split())
M = int(input())
M1 = map(int, input().split())
for k in M1:
    for i in range(N):
        if k == Seat_num1[i]:
            print(Id[i], Seat_num2[i], sep=' ')
