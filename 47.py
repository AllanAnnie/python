dict1 ={}
n = int(input("輸入比數n:"))

for i in range(0,n):
    a = input("請輸入獎牌:")
    b = input("請輸入數量:")
    dict1[a] = b


item1 = list(dict1.items())
for n1,n2 in item1:
    print(str(n1)+"牌得到"+str(n2)+"面")
