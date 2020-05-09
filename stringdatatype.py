mystr="Harry is a good boy"
print(mystr)
print(mystr[4])
#string slicing
print(mystr[0:4]) #index start from 0 and move to 4 words and print all four words
print(mystr[0:5]) #it move to 5 words and print all 5 words
print(mystr[0:19]) #it move its max words and print all character
print(mystr[0:78]) #there is not that uch haracter so it gives all the charater and ignore all
print(mystr[0:5:2]) #it count 5 character and skip 1 character after 0 index and print
print(mystr[0:5:3]) #it count 5 character and skip 2 character after 0 index and print

#advance string slicing
print(mystr[0:]) #it takes first index and automatically take the last index and print all the string between thais index
print(mystr[:5]) #it takes minimum 0 index and maximum 5 index and print all the index between this
print(mystr[::]) #it automaticaaly get starting aur ending index and print all string
print(mystr[::2]) #it also automaticlly get all the string and print the string after skipping one chafacter after 0 index
print(mystr[::3]) #it also automtically get all he string and print string after skipping 2 characters after 0 index
print(mystr[::78]) #it get all the sring and there have no that much character for skip so it skip all the string after 0 index
print(mystr[-4:-2])#it takes character from reverse order last string is called -1 then next is -2 and so on

print(mystr[::-1]) #it reverse th string
print(mystr[::-2]) #it first reverse the sting then skip 1 character and print

#string function
print(mystr.isalnum)#it return boolean value true or false ,it return false because there is a space
print(mystr.isalpha)#it return flso bcoz there is no alpha and no numeric
print(mystr.endswith("boy")) #it returns true because it ends with boy
print(mystr.endswith("body")) #it returns false bcoz it is not ends with body
print(mystr.count("b")) #it return the toal number of b
print(mystr.count("o")) #it also return total number of o
print(mystr.capitalize()) #it make first letter capital
print(mystr.find("is")) #it gives the index where ths "is " is start
print(mystr.lower()) #it changes all strings into lowercase
print(mystr.upper()) #it changes all strings into uppercase
print(mystr.replace("is","are")) #it replace is to are


#length of the string
print(len(mystr))