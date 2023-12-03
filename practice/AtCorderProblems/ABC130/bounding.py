N, X = map(int, input().split())
L = list(map(int, input().split()))
d = 0
count = 1

for i in range(N):
    d += L[i]
    if d>X:
        break
    else:
        count += 1
print(count)