
dict = {"123 456":9000,"456 789":5000,"789 888":6000,"336 558":10000,"775 666":12000,"566 221":7000}
a = int(input(""))
for i in range(a):
    b = input()
    if b not in dict:
        print('error')
    else:
        print(dict[b])