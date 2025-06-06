N = input('Enter a char: ')

if len(N) == 1 and N.isalpha():
    if N == N.lower():
        print("Char is lower")
    elif N == N.upper():
        print("Char is Upper")
else:
    print("Enter valid char")