#try except problem
print("Enter num1")
num1=input()
print("Enter num2")
num2=input()
try:
    print("the sum of these two numbers is ",
          int(num1)+int(num2))
except Exception as e:
    print(e)
print("this line is very important")
