ls = []
"""for i in range(100):
     if i%3==0:
         ls.append(i)
print(ls)
"""
#------------USING LIST COMPEREHENSTION METHOD----------------

"""ls = [i for i in range(100) if i%3==0]
print(ls)
"""
#-----------DICTIONARY COMPEREHENSTION-----------------,it is agood way to make dictionary,
#it also used for reversed key value pairs
"""
dict1 = {i:f"item {i}" for i in range(100)}
dict1 = {i:f"item {i}" for i in range(1, 10001)}
dict1 = {i:f"item {i}" for i in range(1, 10001) if i%100==0}
print(dict1)
dict1 = {i:f"Item {i}" for i in range(5)}
print(dict1)
dict2 = {value:key for key,value in dict1.items()} #it reverse the dictionary value
print(dict1,"\n", dict2)
"""
#-----------------SET COMPEREHENSTION-------------------------
#we use middle brackets for making set comperahension
"""
#dresses = {dress for dress in ["dress1", "dress2","dress1",
 #                              "dress2","dress1", "dress2"]} #it gives output only one time
#print((dresses))
#print(type(dresses))
dresses = [dress for dress in ["dress1", "dress2","dress1",
                               "dress2","dress1", "dress2"]]
print((dresses))
print(type(dresses))
"""
#--------------------GENERATOR COMPEREHENSTION--------------

evens = (i for i in range(100) if i%2==0)#WE USE PARENTHESIS FOR MAKING GENERATOR
"""
print(type(evens))
print(evens)
print(evens.__next__())
print(evens.__next__())
"""
#or we can also write
for item in evens:
     print(item)