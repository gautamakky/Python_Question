my_dict = { 'a':1 , 'b':5, 'c':78,'d':23}
max_value = float('-inf')
max_key = None

for key in my_dict:
    if my_dict[key] > max_value:
        max_value = my_dict[key]
        max_key = key

print(f"The key with the maximum value is: {max_key}")
print(f"The maximum value is: {max_value}")