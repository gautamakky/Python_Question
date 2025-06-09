n = int(input("Enter size of triangle: "))
p=65
for i in range(1,n+1):
    for j in range(i):
        print(chr(p),end=" ")
    print()
    p+=1