a = list(map(int,input("Enter list: ").split()))
if len(a) > 3:
    # max = a[0]
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

    print(a)
    print(f'First larget no is {a[len(a)-1]}\nSecond larget no is {a[len(a)-2]}\nThird larget no is {a[len(a)-3]}')

else:
    print("Enter more than three number")