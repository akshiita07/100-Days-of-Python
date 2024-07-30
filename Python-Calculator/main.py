from art import logo
from replit import clear
import math
# e=2.718 use math.e


# all my operations functions
def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  return a/b
def square(a):    #single parameter fnc
  return a**2
def cube(a):      #single parameter fnc
  return a**3
def squareroot(a):    #single parameter fnc
  return math.sqrt(a)
def exponent(a):      #single parameter fnc
  return (math.e)**a

#creating a dictionary where key:operator and value:fnc
operationsdict={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
  # add sqrt exp
  "sq":square,
  "cu":cube,
  "sqrt":squareroot,
  "exp":exponent,
}
  

#code begins:
# take input for fno and sno and which operation to perform:
def my_calculator():
  print(logo)
  fno=float(input("Enter first number: "))
  # print("+\n-\n*\n/\n") instead of this loop thru dictionary and print keys
  for key in operationsdict:
    print(key)
  
  continuecal=True
  
  while continuecal:
    operation=input("Choose an operation: ")

    if operation not in operationsdict:
      print("Enter a valid operator. Please restart! ")
      my_calculator()
    
    sno=float(input("Enter second number: "))
  
    #pick fnc from dictionary n get ans
    res=operationsdict[operation](fno,sno)
    print(float(fno),operation,float(sno),"=",float(res))
    
    y_or_n=input(f"To ctd calculation with {res} type y or for new calculation type n: ")
  
    if(y_or_n=='n'):
      #clear screen n start new calculation
      clear()
      # continuecal=False
      # instead of exiting calculator i want new calculation to start
      # use recursion
      my_calculator()
    
    elif(y_or_n=='y'):
      #use result res and just ask for second input
      # fno=res
      fno=res
      
    else:
      print("Pls enter either y or n")

#call
my_calculator()
