

n = int(input("Enter a number: "))
count = 0
for i in range(1,n):
    for digit in str(i):
        if digit == '8':
            count += 1
print("Total occurrences of 8 from 1 to 100:", count)