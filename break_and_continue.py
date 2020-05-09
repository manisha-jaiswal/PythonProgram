"""i=0
while(i<10):
    print(i+1,end=" ")
    i=i+1
"""
i=0
while(True):
    if i+1<5:
        i=i+1
        continue

    print(i+1,end=" ")
    if(i==44):
        break
    i=i+1
