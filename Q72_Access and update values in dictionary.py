my_dict = {}

n = int(input("How many items you want to enter in dictionary? "))

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for '{key}': ")
    my_dict[key] = value

print("Dictionary:", my_dict)
key_to_update = input("Enter key to update: ")
new_value = input("Enter new value: ")

if key_to_update in my_dict:
    my_dict[key_to_update] = new_value
    print("Updated:", my_dict)
else:
    print("Key not found!")