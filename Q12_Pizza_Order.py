print("-----------Order your pizza------------")
size = input("Choose the size of Pizza: Small,Medium,Large:")
sizeUpper = size.upper()
if sizeUpper == 'SMALL' or sizeUpper == 'LARGE' or sizeUpper == 'MEDIUM':
    if sizeUpper == 'SMALL':
            bill = 100
            print("You choose Small size pizza.")
    elif sizeUpper == 'MEDIUM':
            bill = 200
            print("You choose Medium size pizza.")
    else:
            bill = 300
            print("You choose Large size pizza.")
    cheese = input("Do you want extra cheese ? (Y/N):")
    cheeseUpper = cheese.upper()
    if cheeseUpper == 'Y':
        if sizeUpper =='SMALL':
            bill += 30
            print(f"You have choose extra cheese for {sizeUpper} pizza")
        elif cheeseUpper =='Y' and sizeUpper =='MEDIUM':
            bill += 50
            print(f"You have choose extra cheese for {sizeUpper} pizza")
        else:
            bill += 80
            print(f"You have choose extra cheese for {sizeUpper} pizza")
    else:
        print("you have not selected extra cheese")
    print(f"Your total bill  is {bill}. Have a good day")
else:
    print("please enter correct size")



