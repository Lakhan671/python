import array;
cars = ["Ford", "Volvo", "BMW"];
x = cars[0];
print(x)
cars[0]="TVS"
x = cars[0];
print(x)
print("______________________________________")
cars.append("Honda")
for x in cars:{
    print(x)
}
print("length of array="+str(len(cars)))
cop=cars.copy();
print(cop)
#cop.clear();
print(cop);
print(cars)
cop.pop(0)
print(cop)


print("--------------------Array module")
student_roll=array.array('f',[10,11])
print(student_roll[0])
for x in student_roll:
     print(x)