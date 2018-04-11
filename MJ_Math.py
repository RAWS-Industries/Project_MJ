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
root = lambda x,y: x**(1/y)


print (root (125,2))

def select_Math (num1, num2, choice):
    if choice == 'plus':
        return num1,"+",num2,"=", add(num1,num2)

    elif choice == 'minus':
        return num1,"-",num2,"=", subtract(num1,num2)

    elif choice == 'times':
       return num1,"*",num2,"=", multiply(num1,num2)

    elif choice == 'powered':
       return num1,"/",num2,"=", divide(num1,num2)

    elif choice == 'root':
       return num1,"**",num2,"=", power(num1,num2)

    else:
       return "Choice invalid"
                                                                
                                                               