N , K = map(int,input().split())
h = list(map(int,input().split()))

dp = [0]+[float('inf')]*(N-1)
for i in range(N):
  for j in range(1,K+1):
    if i+j < N:
      dp[i+j] = min(dp[i+j], dp[i] + abs(h[i]-h[i+j]) )

print(dp[-1])

#pythonがカス過ぎて一生TLE出る　これ以上改善しようがない　pypyを使うことで解決した！！！！