a = int(input("輸入x軸座標:"))
b = int(input("輸入y軸座標:"))
c = a**2+b**2
if a==0 and b==0:
    print("該點位於原點")
elif a>0 and b>0:
    print("該點位於第一象限,離原點距離根號為",c)
elif a<0 and b>0:
    print("該點位於第二象限,離原點距離根號為",c)
elif a<0 and b<0:
    print("該點位於第三象限,離原點距離根號為",c)
elif a>0 and b<0:
    print("該點位於第四象限,離原點距離根號為",c)
elif a>0 and b==0:
    print("該點位於右半平面x軸上,離原點距離根號為",c)
elif a<0 and b==0:
    print("該點位於左半平面x軸上,離原點距離根號為",c)
elif a==0 and b>0:
    print("該點位於上半平面y軸上,離原點距離根號為",c)
elif a==0 and b<0:
    print("該點位於下半平面y軸上,離原點距離根號為",c)