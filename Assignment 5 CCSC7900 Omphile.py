# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:28:32 2024

@author: S1004826
"""
# define functions for operations

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



          
n1 = int(input("Enter first number:"))
                 
n2 =int(input("Enter second number:")) 

result = exp(n1,n2)
numbertype = number_type(result)
print ("Assignment Complete")



  
 
     
         
