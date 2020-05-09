import pickle
#pickle is a built-in module
# Pickling a python object
"""cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]#this is not necessary that it is a liat,it is anything,it may be structure,list,dictionary etc
file = "mycar.pkl"
fileobj = open(file, 'wb') #wb means binary form
pickle.dump(cars, fileobj) #dump takes two obj, 1.obj jo pack krna chahte h, 2. file obj leta h
fileobj.close()
"""
#now we learn that how we depickle it
file = "mycar.pkl" #our file name
fileobj = open(file, 'rb') #here we read file in binary format
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))


# pickle = load is a func in pickle which takes a file obj in a argument and return that obj,
# it is used for storing the data but is not not much good,some times it creates problem
#pickle.loads=pickle.loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict",
# buffers=None)Return the reconstituted object hierarchy of the
# pickled representation bytes_object of an object,
# The protocol version of the pickle is detected automatically, so no protocol argument is needed,
# Bytes past the pickled representation of the object are ignored,
# Arguments file, fix_imports, encoding, errors,
# strict and buffers have the same meaning as in the Unpickler constructor,
# Changed in version 3.8: The buffers argument was added.