n = input("Enter a name: ")
n_new = n
for i in n:
    if i.isdigit():
        n_new = n_new.replace(i,"")
print(n_new)


