n = 5
total = 0
car=[ ]
for i in range(n):
    car.append(input())
    if car[i] == 'A':
        total =total+1
    elif car[i] == 'J':
        total =total+11
    elif car[i] == 'Q':
        total =total+12
    elif car[i] == 'K':
        total =total+13
    elif car[i] == '2':
        total =total+2
    elif car[i] == '3':
        total =total+3
    elif car[i] == '4':
        total =total+4
    elif car[i] == '5':
        total =total+5
    elif car[i] == '6':
        total =total+6
    elif car[i] == '7':
        total =total+7
    elif car[i] == '8':
        total =total+8
    elif car[i] == '9':
        total =total+9
    elif car[i] == '10':
        total =total+10
print(total)