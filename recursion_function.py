"""def print2(str1):
    print ("This is " +str1)
print2("MANU")
"""
#Factorial using Recursion
"""def factorial1(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac
  
    it takes, :parameter n: Integer
                 :return : n * n-1 * n-2 * n-3 *.......*1
    n! = n* n-1 *n-2 * n-3 * .... * 1
    n!= n * (n-1)!
    

number=int(input("Enter a number "))
print("Factorial of a number using iterative approach")
print(factorial1(number))
"""
def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
number=int(input("Enter a number "))
print("Factorial of a number using iterative approach")
print(factorial_recursive(number))