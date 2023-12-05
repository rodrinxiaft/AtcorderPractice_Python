N , K = map(int,input().split())
from math import comb

INF = 10**9 + 7

for i in range(1,K+1):
    ans=comb(N-K+1,i)*comb(K-1,i-1)
    print(ans%INF)