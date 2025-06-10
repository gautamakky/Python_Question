n = list(map(int,input("Enter list: ").split()))
sum = 0
for i in n:
    sum += i
print(f'Average of list element is : {sum/len(n)}')
