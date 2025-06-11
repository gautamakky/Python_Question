def is_perfect(num):
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

n = int(input("Enter a number: "))

if is_perfect(n):
    print(f"{n} is a Perfect Number.")
else:
    print(f"{n} is not a Perfect Number.")

