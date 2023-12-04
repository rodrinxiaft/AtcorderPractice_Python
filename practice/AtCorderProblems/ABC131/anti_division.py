#TLE
import math
A , B , C , D  = map(int,input().split())
whole = B-A+1
lcm = math.lcm(C,D)
for i in range(A,B+1):
    if i%C==0:
        whole -=1
    if i%D==0:
        whole -= 1
    if i%lcm==0:
        whole += 1

print(whole)

#GPT 関数を定義することでfor文を回避
import math

def count_multiples_in_range(start, end, divisor):
    return (end // divisor) - ((start - 1) // divisor)

def lcm(x, y):
    return x * y // math.gcd(x, y)

A, B, C, D = map(int, input().split())

count_C_multiples = count_multiples_in_range(A, B, C)
count_D_multiples = count_multiples_in_range(A, B, D)
lcm_CD = lcm(C, D)
count_lcm_multiples = count_multiples_in_range(A, B, lcm_CD)

result = (B - A + 1) - count_C_multiples - count_D_multiples + count_lcm_multiples
print(result)
