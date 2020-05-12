import numpy as np
import matplotlib.pyplot as plt
from functools import reduce;

class Lagrange_polynomial:
  def lag(x,y,num):
    """
    'num' is a set of given points, use x and y to figure out lagrange
    polynomial and calculate all the corresponding values for num

    Implement as you wish but your 'total' numpy array
    has to return all the results 
    """
    
    assert(len(x)==len(y))
    total  = np.zeros(len(num))
    
    for k in range(len(num)):
      sum=0;
      n=len(x);
      for i in range(n):
        xi,yi=x[i],y[i];
        def L(i):
          val=1;
          for j in range(n):
            if i==j:
              continue;
            xj,yj=x[j],y[j];
            val*=(num[k]-xj)/(xi-xj);
          return val;
        sum+=yi*L(i);
      total[k]=sum;
    
    return total
 

data_x = np.array([-3.,-2.,-1.,0.,1.,3.,4.])
data_y = np.array([-60.,-80.,6.,1.,45.,30.,16.])

#generating 50 points from -3 to 4 in order to create a smooth line
X = np.linspace(-3, 4, 50, endpoint=True)
F = Lagrange_polynomial.lag(data_x, data_y, X)
plt.plot(X,F)
plt.plot(data_x, data_y, 'ro')
plt.show()