# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x=input("");
print(x);
x="he";
print(x+"\np");
x=str(input(""));
print(x);
a="**.,+< CSE*";
print(a[0:3]);
print(a.lstrip("*+,"));
print(a.replace('.',''));
a=a.replace('*','');
print(a);
x=21;
if x==1: print(0);
elif x==2: print(1);
else: print(x);
n=1;
while n<10: print(n); n+=1;
for n in range(1,10):  print(n); print(n,end=" ");  
print("task");
m=0;
n=1;
for n in range(1,3):    
 x=int(input("")); 
 n+=1;
 if x>m: m=x;

print(m);
z=int(input(""));
if z>100 or z<70:print("invalid");
elif z>=90:print("A");
elif z>79: print("B");
elif z>69: print("C");
else: print("invalid");

c=["toy",2];
c.insert(5,False);
print(c[2]);
c.pop();
print(c);