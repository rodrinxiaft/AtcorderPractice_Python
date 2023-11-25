S = input()
f = int(S[:2])
l = int(S[2:]) #文字列もスライスできた

if 1 <= f <= 12: #if文をネストすることが可能
    if 1<= l <= 12:
        print('AMBIGUOUS')
    else:
        print('MMYY')
else:
    if 1<= l <= 12:
        print('YYMM')
    else:
        print('NA')