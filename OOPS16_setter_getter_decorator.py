class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
       # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
 #   @property
  #  def email(self):
   #     return f"{self.fname}.{self.lname}@codewithharry.com"

    @property #it is a property decorator
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter #for use to set the attribute
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

a=Employee("abc","ghi")
#b=Employee("n","p")
print(a.explain())
print(a.email)
a.fname="hj"
print(a.email)
a.email="this.that@gmail.com"
print(a.fname)
print(a.lname)
print(a.email)
del a.email
print(a.email)
a.email="manu.m@gmail.com"
print(a.email)