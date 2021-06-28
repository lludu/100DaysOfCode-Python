#This is day 10 project: Basic Calculator

from replit import clear
from art import logo
#----Calculator

#Addition
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
#Dictionary to call functions
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide,
}



def calculator():
  print(logo)
  print("Welcome to the Python Calculator!\n")
  #User's 1st Number
  num1 = float(input("What's the first number?: "))

  is_calc = True

  while is_calc:
    #Operation Symbols
    symbol_select = '\n+  -  *  /'
    print(symbol_select)
    #Which Operation
    operation_symbol = input("Pick an operation: ")
    #User's Next Number
    num2 = float(input("\nWhat's the next number?: "))
    print("")


    calculation_function = operations[operation_symbol]
    answer = (calculation_function(num1, num2))
    #show original equation and answer
    print(f'{num1} {operation_symbol} {num2} = {answer}\n')

    repeat = input(f"Type 'y' to continue calculating with {answer}, \nor type 'n' to start a new calculation: ").lower()

    if repeat == 'y' or repeat == 'yes':
      num1 = answer
    else:
      is_calc = False
      clear()
      calculator()

calculator()

#Link to Day 10 project
#https://replit.com/@Lludu/calculator#main.py
