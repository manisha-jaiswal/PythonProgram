#global and local variable and global keyword
#--------------------------------------------------------------------------------------------
l=10 #global variable used in everywhere , global scope
def function1(n):
    #l=5 #local variable , it is not used outside the function
    m=8 #local variable
    #l=l+45
    # we cannot change globl variable value,
    # if we want to change value of global variable within the function then we use global keyword
    global l
    l=l+45
    print(l,m)  # here it searches l in function,if its not found then it search outside the function and print value of l,
    print(m,"i have printed")
function1("this is me ,")
print(l)
#--------------------------------------------------------------------------------
# using nestef function
#--------------------------------------------------------------------------------


def Manu():
    x=20
    def Sanu():
        global x #it goes outside and search global value,if find then replace the value 88 else not
        x= 88
    print("before calling sanu()",x)
    Sanu()
    print("after calling sanu()",x)
Manu()
print(x)

