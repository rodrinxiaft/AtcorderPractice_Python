K , G , M = map(int,input().split())

tempG = 0
tempM = 0
for i in range(K):
    if tempG == G:
        tempG = 0
    elif tempM == 0:
        tempM = M
    else:
        if tempG+tempM >= G:
            tempM = tempM - (G-tempG)
            tempG = G
        else:
            tempG = tempM
            tempM = 0
            
print(tempG,tempM)