L , R = map(int,input().split())

mod = 2019
ans = []
if R - L >= mod:
    print(0)
else:
    for i in range(L,R):
        for j in range(i+1,R+1):
            c = (i*j)%mod
            ans.append(c)
    print(min(ans))
