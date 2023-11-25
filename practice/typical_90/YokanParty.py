def max_score(L,N,A,K):
    def check(x): #実行可能かを確認
        num = 0
        pre = 0
        for i in range(N):
            if A[i] - pre >= x: #前回の切れ目から初めてx以上になったら切る
                num += 1
                pre = A[i] #前回の位置を更新
        if L - pre >= x: #最後の切れ目の扱い
            num += 1
            
        return num >= K + 1
#二分探索
    left = -1
    right = L + 1
    while right - left > 1:
        mid = (left + right)//2
        
        if check(mid):
            left = mid #mid > serchなのでleftに絞る
        else:
            right = mid #mid < rightなのでrightに絞る　
            
    return left #leftを返す

L = 100
N = 3
K = 1
A = [28, 54, 81]
print(max_score(L,N,A,K))

N , L = map(int,input().split())
K = int(input())
A = list(map(int,input().split()))

def check(x):
  num = 0
  pre = 0
  for i in range(N):
    if A[i] - pre >= x:
      num += 1
      pre = A[i]
    
  if L - pre >= x:
      num += 1
      
  return (num >= K + 1)

left , right = -1, L + 1
while right - left > 1:
  mid = (right + left)//2
  if check(mid):
    left = mid
  else:
    right = mid
    
print(left)