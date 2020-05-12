

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

f = Polynomial([2.0, 1.0, -6.0, -2.0, 2.5, 1.0])
a = -0.5
b = 1.3
m = (a+b)/2
e = 1e-6

list_a = []
list_b = []
list_m = []
list_f = []

root = 0.0
while True:
  list_a.append(a);
  list_b.append(b);
  list_m.append(m);
  list_f.append(f(m));

  if (f(a)*f(m))<0:
    b = m;
  
  else:
    a=m;
  n=(a+b)/2;
  if (abs(n-m)/abs(n))<e:
    break;
  root=n;
  m=n;

  
   
  
    



#+--------------------+
#| End of your code   +
#+--------------------+

xs = np.linspace(-2.5, 1.6, 100)
ys = f(xs)

plt.axhline(y=0, color='k')
plt.plot(xs, ys)
plt.plot(root, f(root), 'ro')


print(pd.DataFrame({'a':list_a, 'b':list_b, 'm':list_m, 'f(x)':list_f}));
plt.show();
