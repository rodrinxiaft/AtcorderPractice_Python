def count_some_sums (A,B,N):
    sums = 0
    numbers = []
    for i in range(1,N+1):
        judge = 0
        judge = sum(map(int, str(i)))
        if judge >= A and judge <= B:
            numbers.append(i)
    sums = sum(numbers)
    
    return sums
print(count_some_sums(2,5,20))

A,B,N = int(input())

sums = 0
for i in range(1,N+1):
    judge = sum(map(int,str(i)))
    if A <= judge <= B:
        sums += i
print(sums) 