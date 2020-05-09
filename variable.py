var1="hello world, " #string var
var2=4 #integer var
var3=36.7 #float var
var4="herry"
var5="32"
var6="52"
print(type(var1)) #showing the variable type
print(type(var2))
print(type(var3))
print(var1+var4)#concatenate two string
print(var2+var3)#add integer and float
print(var1+var5)#concatenate two string
print(var5+var6)#concatenate two string value

#type casting
print(int(var5)+int(var6)) #convert string into integer and then add
print(str(var2)+str(var3)) #convert integer and float into string then concatenate
print(float(var5)+float(var6)) #convert two string into float then add
print(var1*10) #print sring into 10 times
print(10* int(var5)+int(var6)) #convert strings into integer then add then multiply by 10
print(10* str(int(var5)+int(var6))) #convert string into integer then sum then again convert it into string then print 10 times

#take input from user
print("Enter your number")
inpnum=input()#it always take string

print("you enterd ",inpnum)
#print("you enterd",inpnum+10) #it gives error bcoz one is string and another is integer
print("you entered ",int(inpnum)+10) #here we convert string into integer then add

