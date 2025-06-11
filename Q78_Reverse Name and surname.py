
def rev(n):
    rev = ""
    for i in range(len(n)):
        rev += n[len(n) - i - 1]
    return rev

name = input("Enter name: ").split()
rev_name = ""
for i in range(len(name)):
    rev_name += rev(name[i]) + " "

print(rev_name.strip())