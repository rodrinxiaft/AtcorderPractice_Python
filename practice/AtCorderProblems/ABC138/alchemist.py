N = int(input())
v = list(map(int,input().split()))

while len(v) > 1:
    v = sorted(v)
    v[0] = (v[0]+v[1])/2
    v.pop(1)
print(v[0])