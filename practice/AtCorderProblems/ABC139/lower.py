N = int(input())
H = list(map(int,input().split()))

ans = 0
for i in range(N):
    c = 0
    j = i
    while j < N-1 and H[j] > H[j+1]:
        c += 1
        j += 1
    ans = max(ans,c)
    
print(ans)