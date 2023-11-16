def is_correct(N,Y):
    for x in range(N+1):
        for y in range(N-x+1):
            z = N-x-y
            if 10000*x + 5000*y + 1000*z == Y:
                return print(x,y,z)
            else:
                return print

print(is_correct(9,45000))


N,Y = map(int,input().split())

for x in range(N+1):
    for y in range(N-x+1):
        z = N-x-y
        if 10000*x + 5000*y + 1000*z == Y:
            print(x,y,z)
            exit()
print(-1,-1,-1)