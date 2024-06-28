# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:20:16 2024

@author: S1004826
"""

def Opes_menu():
    print("Operation Menu")
    print("1. Addition +")
    print("2. Subtraction -")
    print("3. Multiplication *")
    print("4. Division /")
    print("5. Modula %")
    print("6. Floor //")
    print("7. Exponent **")


def making_arithmatic():
       oper = input("Enter Choice of operarion:")

       if oper == "":
          print("No selection")

       else :
        num_1 = int(input("Enter first number:"))
        num_2 = int(input("Enter Second number:"))
    
    
        if oper == "+":
            result = num_1 + num_2
            print("Addition of two number is:", result)
            if result % 2 == 0:
                print("Number is Even:", result)
            else:
                print("Number is Odd", result)
        
        elif oper == "-":
            result = num_1 - num_2
            print("Subtraction of two numbers is:", result)
            if result % 2 == 0:
               print("Number is Even:", result)
            else:
              print("Number is Odd", result)

        elif oper == "*":
          result = num_1 * num_2
          print("Multiplication of two numbers is:", result)
          if result % 2 == 0:
              print("Number is Even:", result)
          else:
             print("Number is Odd", result)

        elif oper == "/":
            result = num_1 / num_2
            print("Division of two numbers is:", result)
            if result % 2 == 0:
                print("Number is Even:", result)
            else:
                    print("Number is Odd", result)

        elif oper == "//":
            result = num_1 // num_2
            print("Floor Division of two numbers is:", result)
            if result % 2 == 0:
                print("Number is Even:", result)
            else:
                    print("Number is Odd", result)

        elif oper == "%":
            result = num_1 % num_2
            print("Modula of two numbers is:", result)
            if result % 2 == 0:
                print("Number is Even:", result)
            else:
                print("Number is Odd", result)

        elif oper == "**":
            result = num_1 ** num_2
            print("Exponential of two numbers is:", result)
            if result % 2 == 0:
                print("Number is Even:", result)
            else:
                    print("Number is Odd", result)

def Main():
    while True:
        Opes_menu()
        making_arithmatic()
        another_operation = input("Do you want to perform another operation? (y/n): ")
        if another_operation == 'n':
         print("Thank you for using the calculator!")
        else :
            Main()
        break
         

Main()
print("Assignment Complete")

       

    



