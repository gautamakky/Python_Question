a = list(map(int,input("Enter first list: ").split()))
b = list(map(int,input("Enter second list: ").split()))
c = []
if len(a)==len(b):
    for i in range(len(a)):
        c.append(a[i]-b[i])
    print(f'First list is: {a} \nSecond list is: {b} \nSubtraction of both list is {c}')

else:
    print("List size is not same.")