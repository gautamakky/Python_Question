n = list(map(int,input("Enter numbers to list, spaces separated: ").split()))
num = int(input("Enter a number which you want to check: "))

for i in range(len(n)):
    if n[i] == num:
        index = i
        print(f"{num} is present in this list {n} and the index of {num} is {index}")
        break
else:
    print(f'{num} is not present in the given list.')
