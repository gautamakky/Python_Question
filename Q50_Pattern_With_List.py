name = input("Enter Name: ")
n = len(name)
for i in range(n):
    p = name[i]
    for j in range(i+1):
        print(p,end=" ")
    print()