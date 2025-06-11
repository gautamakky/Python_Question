n = int(input("Enter how many keys you wants to enter in your dictionary: "))
my_dict = {}
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f'Enter value for {key}: ')
    my_dict[key]=value
print(f"Your given dictionary{my_dict}")
x = input("Enter the key you want to delete: ")
if x in my_dict:
    del my_dict[x]
    print(f"After deleteing {x} updated dictionary is: {my_dict}")
else:
    print("Key not present")
