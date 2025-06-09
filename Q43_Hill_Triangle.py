n = int(input("Enter a number: "))
for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for l in range(i):
        print("*",end=" ")
    print()