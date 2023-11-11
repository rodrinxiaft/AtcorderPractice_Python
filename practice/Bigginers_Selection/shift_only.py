def count_attempts(x):
    count = 0
    while all(i%2 == 0 for i in x):
        x = [i//2 for i in x]
        count +=1
    return count
                
print(count_attempts([2,4,6]))

N = int(input())
A = list(map(int, input().split()))

count=0
while all(i%2==0 for i in A):
  A=[i//2 for i in A]
  count +=1

print(count)