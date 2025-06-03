print("-----------Blood Donation----------")

value_A = input("Enter your age:\n")
value_B = input("Enter your weight:\n")
age = int(value_A)
weight = int(value_B)
if value_A.isdigit() and value_B.isdigit():

    if age >= 18 and weight >= 50:
        print("No recent ilness.\n You are eligable to donate blood")
    else:
        print("You are not eligable to donalte blood")

else:
    print("Please input correct input.")