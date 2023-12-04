N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

sortedAB = sorted(AB, key=lambda x: x[1])
count = 0
for i in range(N):
    count += sortedAB[i][0]
    if count > sortedAB[i][1]:
        print('No')
        break 
else:
    print('Yes')