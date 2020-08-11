def add():
    y=20;
    return  lambda x:x+y;
print(add()(7))