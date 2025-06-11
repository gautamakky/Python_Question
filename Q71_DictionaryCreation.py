my_dict = {}

n = int(input("How many items you want to enter in dictionary? "))

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for '{key}': ")
    my_dict[key] = value

print("Dictionary:", my_dict)