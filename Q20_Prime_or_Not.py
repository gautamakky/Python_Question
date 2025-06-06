# Prime or not
N = int(input("Enter a number: "))
if N == 1:
    print("Its not a prime no.")
if N > 1:
    for i in range(2,N):
        if N % i == 0:
            print("Its not prime no")
            break
    else:
        print("Its a prime no")