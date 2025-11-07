def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n = int(input("Enter a Positive number = "))
if n<0:
    print("Factorial is not defined for negative number")
else:
    f=factorial(n)
    print('factorial of',n,"is",f)
