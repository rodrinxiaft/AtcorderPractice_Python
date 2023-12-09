dp = [0]*(N+1)
dp[1] = max(A[0],B[0],C[0])

for i in range(2,N+1):
    if dp[i-1] - dp[i-2] == A[i-2]:
        dp[i] = dp[i-1] + max(B[i-1],C[i-1])
        
    elif dp[i-1] - dp[i-2] == B[i-2]:
        dp[i] = dp[i-1] + max(A[i-1],C[i-1])
        
    elif dp[i-1] - dp[i-2] == C[i-2]:
        dp[i] = dp[i-1] + max(A[i-1],B[i-1])
# print(dp)
print(dp[-1])
#だめだった

N = int(input())
A = [0] * N
B = [0] * N
C = [0] * N
for i in range(N):
    A[i], B[i], C[i] = map(int, input().split())
    
dp = [[0]*3 for i in range(N+1)]

dp[1][0] = A[0]
dp[1][1] = B[0]
dp[1][2] = C[0]

for i in range(1,N):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i+1][k] = max(dp[i+1][k],dp[i][j] + [A[i],B[i],C[i]][k])

print(max(dp[N]))