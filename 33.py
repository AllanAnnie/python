ch =int(input("國文:"))
eg =int(input("英文:"))
mt =int(input("微積分:"))
ph =int(input("體育:"))
py =int(input("程式設計:"))
ag =(ch+eg+mt+ph+py)/5
print("平均分數:",ag)
print("最高分科目",max(ch,eg,mt,ph,py))
print("最低分科目",min(ch,eg,mt,ph,py))
