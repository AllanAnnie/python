qus =input("輸入:")
ans ="1234"
a = 0
b = 0
for i in range(len(qus)):
    if ans[i] == qus[i]:
        a += 1
    elif qus[i] in ans:
        b += 1
print("%dA%dB"%(a,b))