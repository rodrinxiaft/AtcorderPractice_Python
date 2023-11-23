#ランレングス圧縮 データ圧縮の方法の一つ 連続する要素を(値,個数)の順番で返す
def rels(s):
    n = len(s)
    ans = []
    l = 0
    while l<n:
        r = l+1
        while r<n and s[l] == s[r]:
            r += 1
        ans.append((s[l],r-l))
        l = r
    return ans

print(rels('ssssssaaaanniiikkkaaassss'))

# intertools.groupbyで簡単に実装できる
from itertools import groupby
strings = "aabbbbbbbbbbbba"

ans = [(k, len(list(g))) for k,g in groupby(strings)]
print(ans)
