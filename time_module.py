# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)
import time
initial = time.time() #it returns no. of tick
#print(initial)
k = 0
while(k<45):
    print("This is harry bhai")
    time.sleep(2) #it wait 2 seconds then print after that again print
    k+=1
print("While loop ran in", time.time() - initial, "Seconds") #it gives while loop time

initial2 =time.time()
for i in range(45):
    print("This is harry bhai")
print("For loop ran in", time.time() - initial2, "Seconds") #it return for loop time

localtime=time.asctime(time.localtime(time.time())) #here this function time.localtime() convert itinto local time which is a tuple ,
# so asctime convert this tupel into presentable time format,
# time.time count the tick and return it
print(localtime)
