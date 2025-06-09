n = int(input("Enter size of triangle: "))
p = 65
for i in range(1,n+1):
    for j in range(n):
        print(chr(p),end=" ")
        p += 1
    print()
