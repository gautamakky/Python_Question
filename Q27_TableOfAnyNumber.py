Num = int(input("Enter a number: "))
def table(N):
    print(f'The Table of {N} is: ')
    for i in range(1,11):

        print(f'{N} * {i} = {i*N}')

table(Num)