n = list(map(int,input("Enter numbers in tuple: ").split()))
y = []
for i in n:
    y.append((i,i**2))
print(y)