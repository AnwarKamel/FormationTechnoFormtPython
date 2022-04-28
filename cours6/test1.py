def addNumbers(numberA, numberB):
    """ This is comment """
    return numberA + numberB

def greeting(name="Nobody"):
    """
    Greets the person. Uses "Nobody" if no name is given
    """
    return "Hi " + name + "!"

print("1 + 4 =", addNumbers(1, 4))
print('-' * 60)

print("Greeting without argument:", greeting())
print("Greeting with argument:", greeting("Anis Rouan"))
print('-' * 60)
print(addNumbers.__doc__)
