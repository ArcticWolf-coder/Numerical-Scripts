import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Define a polynomial named 'f'
f = Polynomial([2.0, 1.0, -6.0, -2.0, 2.5, 1.0])

# Define the first derivative of polynomial 'f' named 'f_prime'
f_prime = f.deriv(1)

# Draw the X-axis
plt.axhline(y=0, color='k')

# Generate 100 values of x.
x = np.linspace(-2.5, 1.6, 100)

# Calculate y-values of corresponding x-values of f(x).
y = f(x)

# Plot the graph of f(x) using x-values and y-values
plt.plot(x, y)

# Plot the roots of the graph
plt.plot(f.roots(), f(f.roots()), 'ro')

# Print the roots of the function f(x)
print(f.roots())

# Calcuate y-values for corresponding x-values of f'(x).
y = f_prime(x)

# Plot the graph of f'(x)
plt.plot(x, y)

# Plot the roots of f'(x). Notice that, where f'(x) is zero the slop of f(x) is zero.
plt.plot(f_prime.roots(), f_prime(f_prime.roots()), 'bo')

# Print the roots of f'(x).
print(f_prime.roots())

# Start with an initial value
# complete the line below
xk = 5

# Create a list for storing values of x's after each iteration
list_x = [xk, ]

# Create a list for storing values of f(x)'s after each iteration
list_f = [f(xk), ]

while True:
        #+--------------------+
    #| Start of your code |
    #+--------------------+

    # Calculate newer values of xk   
    k=xk-f(xk)/f_prime(xk);
    xk=k;
    list_x.append(xk);
    list_f.append(f(xk));
    er=abs(list_x[-1]-list_x[-2])/list_x[-1] ;
    if er<1e-6:
        break;
    

    # append xk into list_x
    

    # append f(xk) into list_f
    

    # Write the breaking condition; answer should be accurate to 6 decimal places



    #+------------------+
    #| End of your code |
    #+------------------+

df = pd.DataFrame({"x": list_x, "f(x)": list_f})

print(df)
plt.show();