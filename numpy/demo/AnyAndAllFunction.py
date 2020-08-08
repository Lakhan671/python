from numpy import *
a = array([1, 2, 3, 4, 5])
b = array([1, 2, 3, 4, 5])
c=a==b
print(c.all())
bb = array([1, 92, 3, 4, 5])
cc=a==b
print(cc.any())