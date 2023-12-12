N = int(input())

ls = [str(i) for i in range(1,N+1)]
count = 0
for j in ls:
    if len(j)%2 != 0:
        count += 1
        
print(count)