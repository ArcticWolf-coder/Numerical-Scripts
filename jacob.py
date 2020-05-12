import numpy as np
import sympy as sp

# Define x and y as mathematical symbols
vars = sp.symbols('x y')
x, y = vars

# Define the functions 
f = ([x*y - y**3 - 1, x**2 * y + y - 5])

# Initialise Jacobian matrix
J = sp.zeros(len(f),len(vars))

# Fill Jacobian matrix with entries
for i, fi in enumerate(f):
    for j, symbol in enumerate(vars):
        J[i,j] = sp.diff(fi, symbol)

print(J)
# Find the inverse of Jacobian Matrix
J_inv = sp.Matrix.inv(J)

print(J_inv)
# Initialize solution s with starting value x_0 = 2.0 and y_0 = 3.0
s = sp.Matrix([
    0.0,
    5.0
])

i = 0
while i<10:

    # Update f(s_k) using newer values of s_k
    f_sk = sp.Matrix([f[0].subs({x:s[0],y:s[1]}),f[1].subs({x:s[0],y:s[1]})])


    # Calculate value of inverse jacobian, j^-1(sk), j_val
    j_val = J_inv.subs({x:s[0],y:s[1]})

    print(s) 
    
    # Calculate the new value of s using iterative formula
    s = s-j_val*f_sk;

    
    i += 1

print()