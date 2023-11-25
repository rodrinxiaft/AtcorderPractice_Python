N , L , R = map(int,input().split())
A = list(map(int,input().split()))

ans = []
for i in range(len(A)):
    x = min(max(A[i],L),R)
    if abs(x-A[i]) <= abs(L-A[i]) and abs(x-A[i]) <= abs(R-A[i]):
        ans.append(x)
        
print(" ".join(map(str, ans)))

