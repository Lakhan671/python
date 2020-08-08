from numpy import *
a = array([1, 2, 3, 4, 50])
b=a.view();
b[0]=90;
print(a)
print(b)
print("------------------------")
c=a.copy();
c[0]=190
print(a)
print(c)