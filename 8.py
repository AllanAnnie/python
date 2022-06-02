a = int(input("輸入第一行正整數為:"))
b = input("第二行中數列中的數字為:").split()
list1 = []

for i in b:
    c = b.count(i)
    list1.append(c)
print("出現次數",max(list1))
