N , M = map(int,input().split())
S = list(map(int, input()))

plainT = M
logoT = 0
count = 0
for i in range(N):
    if S[i] == 1:
        if plainT == 0:
            count += 1
        else:
            plainT -= 1
    elif S[i] == 2:
        if logoT == 0:
            count += 1
        else:
            logoT -= 1
    elif S[i] == 0:
        plainT = M
        logoT = count

print(count)