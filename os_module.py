#--------------------- OS MODULES -------------------------------
import os
"""
print(dir(os))
print(os.getcwd())
#os.chdir("C://")
print(os.getcwd())
f = open("manu.txt")
print(os.listdir("C://")) #it gives all files
print(type(os.listdir("C://")))
os.makedirs("This/that") #it make subdirectries"""
#os.rename("manu2.txt", "manujais.txt")
print(os.environ.get('Path'))
print(os.path.join("C:/", "/manujais.txt"))
print(os.path.exists("C://Program Files")) #find the path of file
print(os.path.exists("C://Program Files2"))
print(os.path.isfile("C://Program Files"))
