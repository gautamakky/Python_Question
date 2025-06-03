# Q(5). # 2. ATM Withdrawal Simulation
# Problem:
#
# If balance is enough and amount is multiple of 100 → allow withdrawal
#
# If not multiple of 100 → show message
#
# If not enough balance → show error

balance = 1500
amount = int(input("Enter withdrawal amount: "))

if amount > balance:
    print("Insufficient balance")
elif amount % 100 != 0:
    print("Amount must be a multiple of 100")
else:
    balance -= amount
    print("Withdrawn:", amount)
    print("Remaining Balance:", balance)