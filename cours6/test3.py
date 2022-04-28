def factorial(x):
    factorial = 1
    if x < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif x == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, x + 1):
            factorial = factorial * i
    return factorial

# to take input from the user
num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)