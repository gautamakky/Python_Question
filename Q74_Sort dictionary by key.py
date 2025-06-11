my_dict = {
    "John": 25,
    "Alice": 30,
    "Bob": 22,
    "Charlie": 28
}

# Step 1: Extract keys
keys = list(my_dict.keys())

# Step 2: Sort keys manually using Bubble Sort
for i in range(len(keys)):
    for j in range(0, len(keys)-i-1):
        if keys[j] > keys[j+1]:
            keys[j], keys[j+1] = keys[j+1], keys[j]

# Step 3: Create new dictionary in sorted key order
sorted_dict = {}
for key in keys:
    sorted_dict[key] = my_dict[key]

print("Sorted dictionary by key:", sorted_dict)

