from numpy import *
a = array([1, 2, 3, 4, 50])
b = array([11, 2, 3, 4, 5])
result=where(a>b,a,b);
print(result)