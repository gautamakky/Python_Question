a = list(map(int,input("Enter list: ").split()))
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print(a)
print(f'larget no is: {a[len(a)-1]} and smallest no is: {a[0]}')

