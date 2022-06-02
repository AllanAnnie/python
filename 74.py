list1 = ["red","blue","red","green"]
count = 0
for i in range(0,10):
    ans = 0
    a = input("請輸入四個顏色:").split(" ")
    for j in range(0,4):
        
        if list1[j] == a[j]:
            print(1)
            ans += 1
        elif a[j] in list1:
            print(2)
        else:
            print(3)

    if ans == 4:
        a = "正確答案"
        print(a)
        break

    count += 1
    if count == 10:
        print("挑戰失敗")