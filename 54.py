k = float(input("請輸入路程公里數(km):"))
m =75
ns =0
if k < 1.5:
    m =75
else:
    ns =k-1.5
    if ns > 0.25:
        m =m +((ns // 0.25+1)*5)
    elif ns <= 0.25:
        m += 5
print('所需車資為',m)
