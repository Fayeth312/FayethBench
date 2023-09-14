user_input = int(input("Insert first number: "))
user_input2 = int(input("Insert second number: "))
user_input3 = input("What operation are you using?: +, -, *, /: ")

def add():
    print(f'{user_input} + {user_input2} equals {user_input + user_input2}')

def subtract():
    print(f'{user_input} - {user_input2} equals {user_input - user_input2}')

def multiply():
    print(f'{user_input} * {user_input2} equals {user_input * user_input2}')

def divide():
    print(f'{user_input} / {user_input2} equals {user_input / user_input2}')

if user_input3 == "+":
    add()
     
if user_input3 == "-":
    subtract()
      
if user_input3 == "*":
    multiply()
        
if user_input3 == "/":
    divide()