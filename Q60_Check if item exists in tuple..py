n = tuple(map(int,input("Enter numbers in tuple: ").split()))
x = int(input("Check which value you want to check: "))
if x in n:
    print(f"{x} is present")
else:
    print(f"{x} is not present")