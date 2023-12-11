N , S , K = map(int,input().split())
l = [list(map(int, input().split())) for l in range(N)]

cost = 0
for i in range(N):
    cost += l[i][0]*l[i][1]
    
if cost >= S:
    print(cost)
else:
    print(cost+K)