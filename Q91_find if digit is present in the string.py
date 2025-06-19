name = input("enter your name: ")
for i in name:
    if i.isdigit():
        print("string contains digit")
    else:
        print("string not contains digit")