import numpy as np;
a=np.array([1,2,3]);
print(type(a))
print(a);
print(a.shape);
print(a.size);
print(a[0],a[1],a[2]);
#print(a);
c=np.array([[1,2,3],[4,5,6],[7,8,9]]); print(c);
print(c);
print(c.size);
print(c.shape);
d=c.flatten();
print(d);
e=d.reshape(3,3);
print(e);
s=np.zeros((3,3));
print(s);
d=c.copy();
print(d);
d[1:,1:]=0;
print(d);
print(c.max());
print(c.min());
t=np.random.random((3,3));
r=np.linalg.inv(t);
print(t);
print(r);
x=np.array([[1,2],[4,5]]);
print(x*2);
y=np.array([[7,8],[10,11]]);
z=np.add(x,y);
q=np.multiply(x,y);
print(z);
print(q);
#similarly sqrt,sum,dot,log
#must be square matrix for dot or multiply
print(np.dot(x,y));
print(np.sin(x));

f=c[1:,1:3];
print(c);
print(f);

