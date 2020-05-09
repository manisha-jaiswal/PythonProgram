"""import random
random_number=random.randint(0,5)
rand=random.random()*100 #if we use only function random() then it gives value within 0 to 1 ,
# so here we multiply this function *100 , now it give value within 0 to 100
list=["star plus","DDI","Aaj Tak","CodewithHarry"]
choice=random.choice(list)
choice1=random.choices(list)

print(random_number)
print(rand)
print(choice)
print(choice1)
"""
import requests

x = requests.get('https://w3schools.com')

print(x.text)