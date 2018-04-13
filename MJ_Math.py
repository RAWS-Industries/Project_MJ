import math 

# This function adds  
add = lambda x,y: x+y

# This function subtracts 
subtract = lambda x,y: x-y

# This function multiplies 
multiply = lambda x, y: x * y

# This function divides 
divide = lambda x, y: x / y
 
# This function returns the power of a number to another number
power = lambda x, y: x**y

#This function returns a certain root of another number
root = lambda x,y: y**(1/x)

def select_Math (num1, num2, choice):
    if choice == '+':
        return num1,"+",num2,"=", add(num1,num2)

    elif choice == '-':
        return num1,"-",num2,"=", subtract(num1,num2)

    elif choice == '*':
       return num1,"times",num2,"=", multiply(num1,num2)

    elif choice == '/':
        if num2 == 0:
            return "process undefined"
        else:
            return num1,"devided by",num2,"=", divide(num1,num2)

    elif choice == '^':
       return num1," to the power of ",num2,"=", power(num1,num2)

    elif choice == 'root':
        return num1,"root of ",num2,"=", root(num1,num2)

    else:
       return "Choice invalid"
                                                                
                                                               