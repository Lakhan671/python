def dis(name,age):
    print(name,age)

dis(name="Lakhan singh",age=29)

print("-----------default arguments------------------")
def dis(name,age=29):
    print(f"Name:{name}, Age:{age}")

dis(name="Lakhan singh")
dis(name="Lakhan singh",age=39)

def employee(*a):
    for i in a:
        print(i)

employee("Lakhan","Kunal","Nonal")
print("-----------length arguments-------------")
def add(**n):
    print(n['a'])

add(a=12,b=23)