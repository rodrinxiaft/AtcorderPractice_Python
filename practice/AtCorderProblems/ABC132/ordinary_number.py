n = int(input())
P = list(map(int,input().split()))

count = 0
for i in range(1,n-1):
    sp = [P[i-1],P[i],P[i+1]]
    sp_sorted = sorted(sp)
    if sp[1]==sp_sorted[1]:
        count +=1
print(count)