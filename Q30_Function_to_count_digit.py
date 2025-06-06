def digit(n):

    count =0
    for i in range(n):
        if n > 0:
            n = n//10
            count += 1
    return count
num = int(input("Enter a number: "))
print(digit(num))