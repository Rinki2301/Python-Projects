logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  return a/b
def mod(a,b):
  return a%b
check=True
while True:
  if check==True:
    num1=int(input("Whats the first number? :"))
  print('''+\n-\n/\n*\n%''')
  operation=str(input("Pick an Opertion: "))
  num2=int(input("Whats the second number? :"))
  if(operation=="+"):
    ans=add(num1,num2)
    print(f'{num1} + {num2} = {ans}')
  elif(operation=="-"):
    ans=sub(num1,num2)
    print(f'{num1} {operation} {num2} = {ans}')
  elif(operation=="*"):
    ans=mul(num1,num2)
    print(f'{num1} {operation} {num2} = {ans}')
  elif(operation=="/"):
    ans=div(num1,num2)
    print(f'{num1} {operation} {num2} = {ans}')
  elif(operation=="%"):
    ans=mod(num1,num2)
    print(f'{num1} {operation} {num2} = {ans}')
  y_or_n=input("Typer y for calculating with {ans} or n for new calculation : ")
  if y_or_n=="y":
    num1=int(ans)
    check=False
  else:
    check=True
    print("\033[H\033[J")
  