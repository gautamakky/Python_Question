# Head or Tail
import random
select = input('Choose between head and tail: \n')
select_low = select.lower()
l = ['head','tail']
random_outcome = random.choice(l)
if select_low == random_outcome:
    print(f" You choose '{select_low.upper()}' and computer choose '{random_outcome.upper()}' : You Won!!")
else:
    print(f" You choose '{select_low.upper()}' and computer choose '{random_outcome.upper()}' : You Lose!!")