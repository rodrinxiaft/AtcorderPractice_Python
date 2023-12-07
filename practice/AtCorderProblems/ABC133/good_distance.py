from math import sqrt
N , D = map(int,input().split())
X = [list(map(int, input().split())) for _ in range(N)]

count = 0
for i in range(N-1):
    for j in range(i+1,N):
        sum = 0
        for k in range(D):
            sum += (X[i][k]-X[j][k])**2
        for l in range(1,int(sqrt(sum)+1)):
            if sum == l*l:
                count +=1
print(count)
