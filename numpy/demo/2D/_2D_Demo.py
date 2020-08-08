from numpy import *
a = array([[1, 2, 3, 4, 50],
           [1, 2, 3, 4, 50]])
#76
for r in a:
     for c in r:
         print(c)
print("--------------")
for i in range(len(a)):
     for j in range(len(a[i])):
         print(a[i][j])
print("--------------------------------")
aa=zeros((3,2),dtype=int)
for b1 in aa:
    for v in b1:
        print(v)



