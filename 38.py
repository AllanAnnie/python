n = int(input("輸入n個地方(2<=n<=10):"))
s = 0
for i in range(1,n+1):
    k =int(input(" "))
    if (k%9) ==0 or (k%11) ==0:
        s = k
    else:
        s = 0
    print("第",i,"個點",s)