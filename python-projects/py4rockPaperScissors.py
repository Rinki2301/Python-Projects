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
import random

num = int(
    input("Welcome to the RPS! For rock-0, for paper-1 and for scissors-2 "))
if num == 0:
    print(rock)
elif num == 1:
    print(paper)
else:
    print(scissors)
numb = random.randint(0, 2)
print("Computer Choice ")
if numb == 0:
    print(rock)
elif numb == 1:
    print(paper)
else:
    print(scissors)
if (num == 0 and numb == 1) or (num == 1 and numb == 2) or (num == 2
                                                            and numb == 0):
    print("You loose")
elif (num == numb):
    print("Draw")
else:
    print("You Won")
