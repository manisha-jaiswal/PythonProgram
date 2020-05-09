"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""

def gen(n):
    for i in range(n):
       # return i - it returns the value true or false
        yield i #yeh i ko yield krega ,
        # yeild ek generator h jo on the fly  value ko geneerate krega

g = gen(3)
print(g)
#this is iterator
#print(g.__next__())
#print(g.__next__())
#print(g.__next__())
#print(g.__next__()) -it gives error bcoz iterator gives maximum 0 to 2 value


for i in g: #here it no gives error ,we access any number
     print(i)

h = "manu"#here if we use anu integer,it gives error bcoz int object is not iterator
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)