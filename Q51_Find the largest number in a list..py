n = list(map(int,input("Enter numbers to list, spaces seprated: ").split()))
m = n
max = n[0]
for i in range(1,len(n)):
    if max < n[i]:
        max = n[i]
print(f'max value is {max} in this list{m}')

