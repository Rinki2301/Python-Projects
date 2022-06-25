logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
# from replit import clear
#HINT: You can call clear() to clear the output in the console.
# from art import logo
print(logo)
d={}
def calc_win():
#   clear()
  print("\033[H\033[J")
  mx=0
  winner=""
  for key in d:
    bid_amount=d[key]
    if bid_amount >mx:
      mx=bid_amount
      winner=key
  print(f"Winner is {winner} with ${mx}")
ask=True
while ask:
  k=input("Enter the name ")
  v=int(input("Amount of Bid $"))
  d[k]=v
  ans = input("Are there any other bidders ? Yes or No ")
  if ans=="No":
    ask=False
    calc_win()
  else:
    print("\033[H\033[J")
    