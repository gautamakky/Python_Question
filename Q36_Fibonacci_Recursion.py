def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

num = int(input("Enter a number: "))
for i in range(num):
    if i < 0:
        print("Enter +ve value")
    else:
        print(fibo(i)