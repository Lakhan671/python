from numpy import *
#1D to  2D convert
a = array([1, 2, 3, 4, 50,90])
b=reshape(a,(2,3))
print(b)
#1D to 3D
a = array([1, 2, 3, 4, 5,6,7,8,9,10,11,12])
c= reshape(a,(2,3,2))
print(c)
#_______________row and column -------------------
r=int(input("Enter no of row: "));
c=int(input("Enter no of column: "));
a=zeros((r,c),dtype=int)
print(a)

#slice---------
aa=a[0,:]
print(aa)
aa=a[:,0]
print(aa)
#-------------------------------------------------------