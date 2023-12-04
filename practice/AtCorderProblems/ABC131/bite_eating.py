N , L = map(int,input().split())

pie = 0
apple = 0
m = float('inf')

for i in range(N):
    pie += L+i
    if m > abs(L+i):
        m = abs(L+i)
        apple = L+i

ans = pie-apple
print(ans)