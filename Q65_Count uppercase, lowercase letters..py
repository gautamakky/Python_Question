n = input("Enter a name: ")
upper_count = 0
lower_count = 0
for i in n:
    if i.isupper():
        upper_count +=1
    else:
        if i.islower():
            lower_count +=1
print(f'There are {upper_count} uppercase and {lower_count} lowercase letters in this string {n}')

