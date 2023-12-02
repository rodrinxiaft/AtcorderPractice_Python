N ,S ,M ,L = map(int,input().split())

cost = []
for s in range(N//6+2): #range(N)だと考慮できない組み合わせが存在する可能性
    for m in range(N//8+2):
        for l in range(N//12+2):
            if N <= s*6 + m*8 + l*12:
                cost.append(s*S + m*M + l*L)
print(min(cost))