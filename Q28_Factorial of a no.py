Num = int(input("Enter a number: "))
def table(N):
    print(f'The Factorial of {N} is: ')
    sum = 1
    for i in range(1,N+1):
        if N > 0:
            sum = sum * i
            N = N-1
    return sum

print(table(Num))