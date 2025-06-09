n = int(input("enter the number: "))
if n < 0:
    print("Please enter positive no: ")
else:
    sum = 0
    while n>0:
        sum += n
        n -= 1
    print(f'sum of {n}th natural no is {sum}')