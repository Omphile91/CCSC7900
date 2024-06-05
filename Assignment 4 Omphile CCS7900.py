# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:20:16 2024

@author: S1004826
"""

num_1 = int(input("Enter first number:"))
num_2=int(input("Enter second number:"))
oper = input("Enter Operator:")


if oper == "+":
  result = num_1 + num_2
  print("Addition of two numbers is:", result)
  if result % 2 == 0:
      print("Number is Even:", result)
  else:
     print ("Number is Odd", result)


elif oper == "-":
    result  = num_1 - num_2
    print ("Subtraction of two numbers is:", result)
    if result % 2 == 0:
        print("Number is Even:", result)
    else:
       print ("Number is Odd", result)

elif oper == "*":
    result  = num_1 * num_2
    print("Multiplication of two numbers is:", result)
    if result % 2 == 0:
        print("Number is Even:", result)
    else:
       print ("Number is Odd", result)
    
elif oper == "/":
    result  = num_1 / num_2
    print("Division of two numbers is:", result)
    if result % 2 == 0:
        print("Number is Even:", result)
    else:
       print ("Number is Odd", result)
    
elif oper == "//":
    result  = num_1 // num_2
    print("Floor Division of two numbers is:", result)
    if result % 2 == 0:
        print("Number is Even:", result)
    else:
       print ("Number is Odd", result)
    
elif oper == "%":
    result  = num_1 % num_2
    print("Modula of two numbers is:", result)
    if result % 2 == 0:
        print("Number is Even:", result)
    else:
       print ("Number is Odd", result)
    
elif oper == "**":
    result  = num_1 ** num_2
    print("Exponential of two numbers is:", result)
    if result % 2 == 0:
        print("Number is Even:", result)
    else:
       print ("Number is Odd", result)
  
else:
    print("Invalid selection")
print("Assignment Complete")

    