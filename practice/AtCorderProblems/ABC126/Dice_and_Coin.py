# N , K = map(int,input().split())

N = 3
K = 10
ans = 0
for i in range(1,N+1):
    count = 0
    while i * 2**count <K:
        count += 1
    ans += 1/N * 0.5**count
print(ans)