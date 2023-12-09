N = int(input())
H = list(map(int,input().split()))

dp = [float('inf') for _ in range(N)]
dp[0]=0
for i in range(1,N):
    dp[i] = min(abs(H[i]-H[i-1])+dp[i-1],dp[i])
    if i >1:
        dp[i] = min(abs(H[i]-H[i-2])+dp[i-2],dp[i])
print(dp[-1])