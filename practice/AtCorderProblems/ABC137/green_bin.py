N = int(input())
s = [''.join(sorted(input())) for _ in range(N)]
import collections

c = collections.Counter(s)
ans = 0
for i in c.values():
    if i >1:
        ans += (i**2-i)//2
print(ans)