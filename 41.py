t = int(input("搭了幾次電梯(1<=t<10):"))
m = 20
for i in range(t):
    s =int(input(" "))
    if s + 1 :
        m =m+20
    elif s +2:
        m =m+40
    elif s - 1:
        m =m-10
print(m)
