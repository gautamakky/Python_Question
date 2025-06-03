print("--------  BMI Tester ---------")
Weight = int(input("Enter your weight in KG: \n"))
Height = float(input("Enter your Height in meters: \n"))

BMI = (Weight/Height**2)
print(f"Your BMI is {BMI}")

if BMI < 18.5:
    print("You are underweight")
elif BMI >18.5 and BMI<24.9:
    print ("You are Normal weight")
elif BMI >24.9 and BMI<29.9:
    print ("You are Overweight")
else:
    print("You need a doctor")