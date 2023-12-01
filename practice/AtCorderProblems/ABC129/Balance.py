N = int(input())
W = list(map(int,input().split()))

total_w = sum(W)
prefiz_sum = 0
min_difference = float('inf')

for i in range(N-1):
    prefiz_sum += W[i]
    difference = abs(total_w - prefiz_sum * 2)
    min_difference = min(min_difference,difference)

print(min_difference)