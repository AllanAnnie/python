n = int(input())

for k in range(1,n-1,2):
    print(" "*3,k)
for i in range(1,n+1,2):
    print(i,end="")
for j in range(n-2,0,-2):
    print(j,end="")
print()
for l in range(n-2,0,-2):
    print(" "*3,l)