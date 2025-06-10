from itertools import count

n = tuple(map(int,input("Enter numbers in tuple: ").split()))
x = int(input("enter a value you want to count: "))
count = 0
for i in n:
    if i == x:
        count += 1
if count <= 0:
    print(f'{x} is not present in the list')
else:
    print(f'{x} is occuring {count} times in this list: {n}')



