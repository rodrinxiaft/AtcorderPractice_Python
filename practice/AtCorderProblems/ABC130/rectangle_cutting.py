#W , H , x , y = map(int,input().split())
W = 2
H = 3
x = 1
y = 2
x1 = x*H
x2 = (W-x)*H
x_max = min(x1,x2)

y1 = y*W
y2 = (H-y)*W
y_max = min(y1,y2)

if x_max == y_max:
    print(x_max,'',1)
else:
    print(max(x_max,y_max),'',0)
