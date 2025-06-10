text = input("Enter your name: ")
my_dict = {}
for char in text:
    if char.isalpha():
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
print(my_dict)