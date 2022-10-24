# Write a program to calculate Integral of a function.

from sympy import symbols,integrate

# specify the symbolic symbol
x= symbols('x')

# create the symbolic function
'''
  fun = x^2 + x + 1
'''
fun = x**2 + x + 1 

print('Input Function')
print(fun)


# perform integration 
integral = integrate(fun, x)


print('Integral of the function')
print(integral)
