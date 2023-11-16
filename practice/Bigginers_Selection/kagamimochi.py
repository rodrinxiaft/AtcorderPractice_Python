def mochi_count (l):
    unique_list  = set(l)
    return len(unique_list)

print(mochi_count([50,30,50,100,50,80,30]))

#何故か全く通らなかった、REなので標準入力ミスかもしれないが他の人も同じ記述しているので謎
mochi_list = []
N = map(int, input())

for i in range(N):
    mochi_list.append(int(input()))
    
unique_list = set(mochi_list)
print(len(unique_list))



