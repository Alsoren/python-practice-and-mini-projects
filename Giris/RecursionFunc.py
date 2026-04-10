def recFunc(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * recFunc(n - 1)
    
x = int(input("Enter a number: "))
print("Factorial of", x, "is", recFunc(x))

x = 27.23
y = x / 3
print(y)