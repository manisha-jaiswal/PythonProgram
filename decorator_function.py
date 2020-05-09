"""def func1():
    print("Subscribe now ")
func2=func1
del func1
func2()
"""
"""
def funcret(num):
    if num==0:
        return print
    if num==1:
        return int
    if num==2:
        return sum
a=funcret(2)
print(a)
"""
"""
def executor(func):#hm function ko as a paramter use kr skte h,aur func ko return v kr skte h
    func("this") #aur hum function ke andar function v dal skte h
executor(print)
"""
#-----------------------DECORATOR-------------------------------
def dec1(func1):
    def nowexec():
        print("Executive now")
        func1()
        print("Executed")
    return nowexec
@dec1
def who_is_manu():
    print("Manu is a good girl")
#who_is_manu()
#who_is_manu=dec1(who_is_manu)
who_is_manu()