A , B , C = map(int,input().split())

if A-B >= C:
    print(0)
else:
    C = C - (A-B)
    print(C)