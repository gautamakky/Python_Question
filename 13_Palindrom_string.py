# Palindrom
n = input("Enter your number")
lenght = len(n)
new_n = ""
for i in range(lenght):
    new_n = n[i] + new_n
if new_n == n:
    print("It is a palindroom")
else:
    print("It is not a palindrom")

# ----------------------------------------