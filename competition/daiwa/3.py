N = int(input())
A = list(map(int,input().split()))
for i in A:
    ans = [j for j in A if j > i]
    print(sum(ans), end=" ")
#TLEだった

from collections import Counter
c = Counter(A)
an = {}
s= 0
for v , t in sorted(c.items(),reverse=True):
    an[v]=s
    s += v*t
print(" ".join(str(an[x])for x in A))