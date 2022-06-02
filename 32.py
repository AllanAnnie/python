a = int(input('小明身上有幾元:'))
b = int(input('販賣機有幾種飲料:'))
d = 0
for i in range(b):
    c = int(input(" "))
    if a>=c:
        d += 1
print(d)
