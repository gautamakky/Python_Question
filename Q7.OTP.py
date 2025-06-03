import random
n = int(input("Enter length of OTP: "))
otp = ""
for i in range(n):
    otp += str(random.randint(0, 9))
print("OTP:", otp)