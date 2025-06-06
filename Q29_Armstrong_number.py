
n = int(input("Enter a number: "))
for num in range(n):
    sum = 0
    org = num
    for i in range(num):
        if n > 0:
            sum = sum + num%10

