#forloop with else
#forloop ke sath else tv kaam krega jb forloop normally end ho,yani ki forloop ko koi break stmt na mile
#for loop 2 trh se end ho skta h
#1. jb sare elements khatm ho jaye
#2.jb hme break statement mil jaye
khana = ["roti", "Sabzi", "chawal"] #it is a list
"""for item in khana:
    print(item)
    #if item == "rotiroll":
       # break

else:
    print("this forloop ended properly")
"""
"""
for item in khana:
    print(item)
    break#it only takes 1 element and print and break loop and execute the program,not go else part
else:
    print("this forloop ended properly")
 """
for item in khana:
    #print(item)
    #if item == "roti":
    if item =="rotiroll":
        break
else:
    print("Your item was not found")

