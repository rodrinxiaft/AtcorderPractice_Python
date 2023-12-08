N = int(input())
A = [int(input()) for _ in range(N)]

A_sorted = sorted(A)
A_max = A[0]
A_sec = A[1]

for i in A:
    if i == A_max:
        print(A_sec)
    else:
        print(A_max)