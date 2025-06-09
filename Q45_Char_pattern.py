n = int(input("Enter a number: "))
for i in range(n-1):
    for j in range(1,n-i):
        print(" ",end=" ")
    for k in range(i+1):
        print(chr(65),end=" ")
    for l in range(i):
        print(chr(66),end=" ")
    print()
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i):
        print(chr(67),end=" ")
    for l in range(n-1-i):
        print(chr(68),end=" ")
    print()