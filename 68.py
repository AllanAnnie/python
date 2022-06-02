qus =input("請輸入第一組數字:")
ans =input("請輸入第二組數字:")
a = 0
b = 0
for i in range(len(qus)):
    if ans[i] == qus[i]:
        a += 1
    elif qus[i] in ans:
        b += 1
print("%dA%dB"%(a,b))
if a ==4:
    print("全對")
else:
    print("加油")
        