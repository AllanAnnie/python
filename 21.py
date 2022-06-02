dict1 = {"123TomDTGD":123,"456CatCSIE":456,"789NanaASIE":789,"321LimDBA":321,"654WonFdd":654}
n=int(input("輸入查詢學號為:"))
if n in dict1:
    print("學生資料為:",dict1)
else:
    print("查無此學號")
    