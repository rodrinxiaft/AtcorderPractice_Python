A ,M ,L ,R = map(int,input().split())
ans = []
if R <= A:
    for i in range(L,A,M):
        ans.append(i)
        ans = ans - [j for j in range(R,A,M)]
elif L <= A <= R:
    for i in range(L,R,M):
        ans.append(i)
elif A <= L:
    for i in range(A,R,M):
        ans.append(i)
        ans = ans - [j for j in range(A,L,M)]
        
print(len(ans))
    