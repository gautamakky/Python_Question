# Q(4).Write a program to find the greatest of four numbers entered by the user.

a,b,c,d = map(int,input("Enter 4 numbers a,b,c,d: \n").split())

if a>b and a>c and a>d:
    print("a is greator")
elif b>c and b>d:
    print("b is greator")
elif c>d:
    print("c is greateor")
else:
    print("d is greator")