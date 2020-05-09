#example of built in function
a=9
b=8
c=sum((a,b)) #here it always take any list ,tuple or iterable so here we used two parenthesis ,
# one for sum function and another for iterable , here press control and click on sum then u go to builtin function of sum
print(c)

#example of user defined function
def function1():
    print("hello function 1")
function1()
function1()
function1()
#print(function1())

#taking input using function which is non return type
def function2(a, b):
    print("sum of function2 is ",a+b)
function2(5,6)

#non return type function
def function3(a,b):
    average=(a+b)/2
    print("Average is ", average)
function3(5,7)

#return type function
def function4(a,b):
    """this is a function which is calculate averag of two numbers
    this is not work for three numbers """ #this is not comment , example of docstring
    average=(a+b)/2
   # print("Average is ", average)
    return average
v=function4(5,11)
print(v)
print(function4.__doc__)
#DOCSTRING-t is used in first line of function using """stmt""".it is used for knowing about the function work,
# we print it using print(function_name.__doc__) , here__ is double underscore
