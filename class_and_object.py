#---------------------INTRODUCTION TO OOPS----------------------
"""
CLASSES-TEMPLATE
OBJECT- INSTANCE
DRY-DONOT REPEAT
"""
class Student:
    pass #pass means nothing in the class
harry=Student() #object of class Student
larry=Student()
print(harry,larry) #it print the location of each object

harry.name="MAnisha" #instance variable
harry.section=1
print(harry.name)
print(harry.section)
larry.subject=["Hindi","English","Maths"]
larry.name="Avinash Shivam"
print(larry.subject,"and name is ",larry.name)
print(harry.name,"Loves",larry.name)