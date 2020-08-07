from array import *
import numpy
student_roll=array('f',[10,191])
print(student_roll[0])
student_roll.append(2010)
for x in student_roll:
     print(x)

tstArray=array('i',[]);
userInput=int(input("Enter size of array : "))
for x in range(userInput):
    tstArray.append(int(input("Enter your number: ")))

for y in  tstArray:
    print(y)