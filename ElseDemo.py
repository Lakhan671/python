m=int(input("enter true or false value"))
if(m):
    print("true condition")
else:
    print("else condition")
    if(m):
        print("nested if")
    else: print("nested else")