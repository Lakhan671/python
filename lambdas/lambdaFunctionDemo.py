sq=lambda x:x*x;
print(sq(3))

sum=lambda x,y:(x+y,x-7)
print(sum(4,4))
add=lambda x=10:(lambda y:x+y)
print(add()(2))
d=add();
print(d(6))
print(d)