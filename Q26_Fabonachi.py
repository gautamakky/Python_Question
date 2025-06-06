first = int(input("Enter first no: "))
second = int(input("Enter second no: "))
third = 0
print(first,second,end=" ")
for i in range(10):
    third = first + second
    print(third,end=" ")
    first = second
    second =third