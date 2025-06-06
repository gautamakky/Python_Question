
n = int(input("Enter Number: "))
N = n
new_n = 0
length = len(str(N))
for i in range(length):
        digit = N%10
        new_n = new_n * 10 + digit
        N = N//10

if n == new_n:
    print("Number is a palindrom")
else:
    print("Number is not a palindrom")