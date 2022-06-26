logo='''
   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  
'''
Easy=10
Hard=5
from random import randint

def set_difficulty():
  difficulty=input("Choose difficulty -> 'easy' or 'hard': ")
  if difficulty == 'easy':
    return Easy
  else:
    return Hard
    
def game():
  print(logo)
  print("Welcome to the Number Guessing game!")
  print("I'm thinking of a number between 1 to 100")
  turn = set_difficulty()
  answer = randint(1,100)

  guess=0
  while guess !=answer:
    print(f"You have {turn} attempts, keep guessing number.")
    guess=int(input("Make a guess: "))
    turn=check_ans(answer,guess,turn)  
    if turn==0:
      print("Not more attempts...You lose")
      break
    elif answer!=guess:
      print("Guess Again")
  
def check_ans(answer,guess,turn):
  if answer > guess:
    print("Too low")
    return turn-1
  elif answer < guess:
    print("Too high")
    return turn-1
  else:
    print("You win!!!!")
    print(f"Answer is {answer}")

game()

