# N = int(input())
# P = list(map(int,input().split()))
N = 5
P = [1,2,3,4,5]

def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

if is_sorted(P):
    print('Yes')
else:
    for i in range(N-1):
        for j in range(N-1):
            temp = P[i]
            P[i] = P[j]
            P[j] = temp
            if is_sorted(P):
                print('YES')
                exit()
            temp = P[i]
            P[i] = P[j]
            P[j] = temp               
    print('NO')