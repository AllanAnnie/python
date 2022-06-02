dict1 ={}
n = int(input("輸入比數n:"))

for i in range(0,n):
    a = input("請輸入獎牌:")
    b = input("請輸入數量:")
    dict1[a] = b


for i in dict1:
    print(i,"牌得到",dict1[i],"面")