#Lambda function or Anonymous functions
#adding two numbers
#def add(a,b):
 #   return a+b

#minus=lambda x,y:x-y
#print(minus(9,4))

#LIST OF LAMBDA
"""def a_first(a):
    return a[1]
a=[[1,41],[5,6],[8,23]]
a.sort(key=a_first)
print(a)
"""
a=[[1,1],[5,6],[8,23]]
a.sort(key=lambda x:x[1])
print(a)
