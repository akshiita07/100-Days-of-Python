rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

userChoose=int(input('What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.'))
print("You chose: ")

if userChoose<0 or userChoose>2:
  print("ENter valid number. You lost")
elif userChoose==0:
  print(rock)
elif userChoose==1:
  print(paper)
else:
  print(scissors)

import random
#computer chooses random
comp=random.randint(0,2)
print("Computer choose: ")

if comp==0:
  print(rock)
elif comp==1:
  print(paper)
else:
  print(scissors)
 
#Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

if userChoose==comp:
  print("Its a tie!")
elif userChoose==0 and comp==2:
  print("You win!")
elif userChoose==2 and comp==1:
  print("You win!")
elif userChoose==1 and comp==0:
  print("You win!")
else:
  print("You LOST")
        