import math
D = int(input())

R = math.sqrt(D) + 1
ans = float('inf')

for x in range(int(R)):
    y = int(math.sqrt(D - x**2))
    if abs(x**2 + y**2 - D) < ans:
        ans = abs(x**2 + y**2 - D)
        
print(ans)