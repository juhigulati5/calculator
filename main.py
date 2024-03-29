from art import logo

print(logo)


def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  
  keep_going = True
  while keep_going:
    
    which_op = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    answer = operations[which_op](num1,num2)
    print(f"{num1} {which_op} {num2} = {answer} ")
    another_round = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    
    if another_round == 'n':
      keep_going = False
      calculator()
    else:
      num1 = answer
    
calculator()
