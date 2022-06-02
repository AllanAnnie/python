list1 = []
for i in range(1,11):
    a = int(input("請輸入第"+str(i)+"個數字:"))
    list1.append(a)

list1.sort(reverse=True)
print("最大的3個數字",list1[0],list1[1],list1[2])
print("最小的3個數字",list1[7],list1[8],list1[9])