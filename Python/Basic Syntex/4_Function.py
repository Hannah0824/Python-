# def add_and_print (a, b, c) : #add_and_print is the name of function            # (a, b, c)= parameter (there are 3 parameters)
#     result = a + b + c
#     print(result)       #(result) is an argument 

# x = 13.2 
# y = 21.4 
# z = 90

# add_and_print(x, y, z) #there has to be the same # of arguments and parameters              # (x, y, z) = arguments (3 arguments) 

def add_and_print (a, b, c) : 
    result = a + b + c     
    return result

x = float(input('Enter first number : '))
y = float(input('Enter second number : '))
z = float(input('Enter third number : '))

print(add_and_print(x, y, z)) 