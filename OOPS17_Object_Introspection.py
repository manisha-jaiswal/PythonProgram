#introsection - type,id,dir
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


a = Employee("manisha", "jaiswal")
print(a.email)
print(type(a))
print(type('this is a string'))
b = "this is a string"
print(dir(b))
print(dir(a))
print(id("that that"))
print(id("that that"))

import inspect
print(inspect.getmembers(a)) #get member is a function