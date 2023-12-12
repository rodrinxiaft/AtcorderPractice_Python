N = int(input())
h = list(map(int,input().split()))

def staris ():
    for i in range(N-2,-1,-1):
        if h[i] > h[i+1]+1:
            return 'No'
        elif h[i] == h[i+1]+1:
            h[i] -= 1
    return 'Yes'

print(staris())