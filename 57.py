dict1={"1A":"127","1B":"130","2A":"117","2B":"130","3A":"137","3B":"150","4A":"99","4B":"112","5A":"115","5B":"128"}
n =0 
s =0
total =0
a =input("請選擇主餐及升級的套餐:")
if a in dict1:
    n =int(dict1[a])
b = input("是否升級成大杯飲料:")
if b == "是":
    s =n+7
elif b == "否":
    s =n
c = input("是否換成大薯:")
if c =="是":
    total =s+13
elif c =="否":
    total =s
print("總共為"+str(total)+"元")