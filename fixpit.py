# -*- coding: utf-8 -*-
"""lab6B.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13GdeGlRUzt1Naw5YFzzsALPKT1dLmrut
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

f = Polynomial([2.0, 1.0, -6.0, -2.0, 2.5, 1.0])
g1 = Polynomial([-2.0, 0.0, 6.0, 2.0, -2.5, -1.0])

def g2(x):
  p = Polynomial([2.0, 1.0, 0.0, -2.0, 2.5, 1.0])
  return np.sqrt(p(x)/6)

def g3(x):
  p = Polynomial([-2.0, -1.0, 6.0, 2.0, 0.0, -1.0])
  return np.power(p(x)/2.5, 1.0/4.0)

a1 = 0.8
g1_a = []

a2 = 0.8
g2_a = []

a3 = 0.8
g3_a = []

#+----------------------+
#| Start of your code   +
#+----------------------+
for m in range(0,20):
  g1_a.append(a1);
  a1=g1(a1);
  g2_a.append(a2);
  a2=g2(a2);
  g3_a.append(a3);
  a3=g3(a3);




#+--------------------+
#| End of your code   +
#+--------------------+

xs = np.linspace(-2.5, 1.6, 100)
ys = f(xs)
dictionary = {
    'x': xs,
    'y': ys
}
plt.axhline(y=0, color='k')
plt.plot(xs, f(xs), label='f(x)')
plt.plot(xs, g1(xs), label='g1(x)')
plt.plot(xs, g2(xs), label='g2(x)')
plt.plot(xs, g3(xs), label='g3(x)')
plt.legend()
if len(g1_a) > 0:
  root = np.array([g1_a[len(g1_a)-1], g2_a[len(g2_a)-1], g3_a[len(g3_a)-1]])
  plt.plot(root, f(root), 'ro')

print(pd.DataFrame({'g1(x)':g1_a, 'g2(x)':g2_a, 'g3(x))':g3_a,}))
plt.show();