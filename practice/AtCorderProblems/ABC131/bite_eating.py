N , L = map(int,input().split())

fla = [L+i-1 for i in [j for j in range(1,N+1)]]
m = float('inf')
for i in range(N):
    d= abs(sum(fla[:i]+fla[i+1:])-(sum(fla)-fla[i]))
    m = min(m,d)
print(m)