def zero_count(n):
    count = 0
    new_digit = str(n)
    for i in new_digit:
        if i == '0':
            count +=1
    return print(f' count of zero is {count}')

num = int(input("Enter a number: "))
zero_count(num)