n = list(map(int,input("Enter a list: ").split()))
odd = []
even = []

for i in range(len(n)):
    if (n[i]%2==0) :
        even.append(n[i])
    else:
        odd.append(n[i])
print(f'Given list: {n}\nOdd list: {odd}\nEven list: {even}')
