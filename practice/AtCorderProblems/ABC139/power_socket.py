A , B = map(int,input().split())

ans = 1
for i in range(40):
    if ans >= B:
        break
    ans += A -1
print(i)