n = list(map(int,input("Enter numbers to list, spaces separated: ").split()))
my_dict = {}
for i in range(len(n)):
    my_dict[n[i]] = i
print(my_dict)