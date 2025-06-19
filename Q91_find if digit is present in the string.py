name = input("enter your name: ").split()
for i in name:
    for j in i:
        if j.isdigit():
            print(i,end=" ")
            break

