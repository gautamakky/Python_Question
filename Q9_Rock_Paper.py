# rock paper scissors
import random

print("------------Lets Play Rock Paper Scissors---------------")
print("Rules are: \n1.Rock wins against scissors.\n2.Scissors wins against Paper.\n3.Paper wins against Rock.\n----------------------------------------------")
choose = input("Select any one: \n")
you_selected = choose.upper()
print(f"You have selected {you_selected} ")
l = ['ROCK','PAPER','SCISSORS']
computer_chooses = random.choice(l)
print(f"Computer choose {computer_chooses} ")
# rusult = ''
if you_selected == 'ROCK':
   if computer_chooses == 'ROCK':
        print("Its a tie!!!")
   elif computer_chooses == 'PAPER':
        print("You loose this round!!!")
   else:
        print("You won this round!!!")
elif you_selected == 'PAPER':
    if computer_chooses == 'ROCK':
        print("You won this round!!!")
    elif computer_chooses == 'PAPER':
        print("Its a tie!!!")
    else:
        print("you loose this round.")
elif you_selected == 'SCISSORS':
    if computer_chooses == 'ROCK':
        print("You loose this round!!!")
    elif computer_chooses == 'PAPER':
        print("You won this round!!!")
    else:
        print("Its a tie!!!")
else:
    print("Please enter correct input.")