def difference_count(N,A):
    Alice_list = sorted(A,reverse=True)[0:N+1:2]
    Bob_list = sorted(A,reverse=True)[1:N+1:2]
    difference = sum(Alice_list) - sum(Bob_list)
    return difference

print(difference_count(3,[2,7,4]))

N = int(input())
A = list(map(int, input().split()))

Alice_list = sorted(A,reverse=True)[0:N+1:2]
Bob_list = sorted(A,reverse=True)[1:N+1:2]
difference = sum(Alice_list) - sum(Bob_list)

print(difference)