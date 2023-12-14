N = int(input())
A = list(map(int,input().split()))

denominetor = 0
for i in range(N):
  denominetor += 1/A[i]

print(float(1/denominetor))