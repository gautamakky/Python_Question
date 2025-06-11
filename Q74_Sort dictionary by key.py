n = int(input("Enter how many keys you wants to enter in your dictionary: "))
my_dict = {}
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f'Enter value for {key}: ')
    my_dict[key]=value
print(f"Your given dictionary{my_dict}")

keys = list(my_dict.keys())

for i in range(len(keys)):
    for j in range(0, len(keys)-i-1):
        if keys[j] > keys[j+1]:
            keys[j], keys[j+1] = keys[j+1], keys[j]

sorted_dict = {}
for key in keys:
    sorted_dict[key] = my_dict[key]

print("Sorted dictionary by key:", sorted_dict)

