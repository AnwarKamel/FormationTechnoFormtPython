A = []  # empty List
numbers = [1, 25, 20, 60, 50]  # List of Integer
names = ['Mohammed', 'Achraf', 'Chamso']  # List Of String
# printing
print(A)
print(numbers)
print(names)
print("-------------------------")
print("List names length = ", len(names))
names.append("Anis")
names.append("Fethi")
print(names)
print("List names length = ", len(names))
print("---------------------------------")
names.remove("Fethi")
print(names)
print("List names length = ", len(names))
print("---------------------------------")
print(numbers) # print List numbers
numbers.sort() # sort List numbers
print(numbers)
numbers.sort(reverse=True)
print(numbers)

