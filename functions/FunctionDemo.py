def getName():
    return "my  name is lakhan singh";


def getSquire5(a:int):
      return a*a;

def changeRef(a:int,b:int):
    a=a+b;
    b=a-b;
    a=a-b;
    print(a)
    print(b)

a:int=90;

print(getSquire5(a))
print(getName())
b=100;
changeRef(a,b)
a=a+b;
b=a-b;
a=a-b;
print(a)
print(b)