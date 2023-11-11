def count_combinations(A,B,C,X):
    count = 0
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                if 500*a + 100*b + 50*c == X:
                    count +=1
    return count

print(count_combinations(30,40,50,6000))

A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0
for a in range(A+1):
  for b in range(B+1):
    for c in range(C+1):
      if 500*a+100*b+50*c == X:
        count +=1
        
print(count)