f1 = open("manu.txt")

try:
    #f = open("do.txt")
    f=open("do2.txt")

except EOFError as e: #we can write more than one cache
    print("Print eof error aa gaya hai", e)

except IOError as e: #this is a types of error
    print("Print IO error aa gaya hai", e)

except Exception as e:
    print(e)
else: #this will run if except is not running
    print("This is else part , it will run only if except is not running")

finally: #it is used for code cleanup
    print("this is finally , it Run  anyway...")
    #f.close()
    f1.close()
print("Important stuff")
