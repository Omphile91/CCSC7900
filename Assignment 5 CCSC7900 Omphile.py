# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:28:32 2024

@author: S1004826
"""
# define functions for operations














def get_typing():
            n1= int(input("Enter first number:"))
            n2 =int(input("Enter second number:")) 
            return n1, n2


def add(n1, n2):
     result = n1 + n2
     print("The addition of two numbers is:", result)  
     return result
 
def subt(n1, n2):
    result = n1 - n2
    print("The subtraction of two numbers is:", result)
    return result

def mult(n1,n2):
    result = n1 * n2
    print("The multiplication of two numbers is:", result)
    return result

def div(n1, n2):
    result = n1 / n2
    print("The division of two numbers is:", result)
    return result

def flor(n1,n2):
    result = n1 //n2
    print("The floor of two numbers is:", result)
    return result

def Mod(n1,n2):
    result = n1 % n2
    print("The modula of two numbers is:", result)
    return result


def exp(n1,n2):
    result = n1 ** n2
    print("The exponential of two numbers is:", result)
    return result
   

# check Even/Odd

def number_type (result):
    if result % 2 ==0:
        print("The number is Even")
    elif result % 2 != 0:
        print ("The number is Odd")

# def main():
#     while True:
#         display_menu()
#         operation = int(input("Enter the operation number (1-7): "))
#         num1, num2 = get_user_input()
#         result = perform_operation(num1, num2, operation)
#         print(f"Result: {result}")
#         print(f"Is result odd? {'Yes' if is_odd(result) else 'No'}")
#         another_operation = input("Do you want to perform another operation? (y/n): ")
#         if another_operation.lower() != 'y':
#             print("Thank you for using the calculator!")
#             break

          
def get_typing():
            n1= int(input("Enter first number:"))
            n2 =int(input("Enter second number:")) 
            result = exp(n1,n2)
            
# numbertype = number_type(result)
# print ("Assignment Complete")



  
 
     
         
