message = "      Hello how are you ahmed   "
print(message.lstrip())
print(message.rstrip())
print(message.strip())

print("----------- startswith -----------")
title = "Python is Easy"
print(title.startswith('Python'))
print(title.startswith('Java'))

print("----------- endswith -----------")
print(title.endswith('Easy'))
print(title.endswith('Easyyy'))

print("----------- istitle -----------")
title = "Python is Easy"
title2 = "Python Is Easy"
print(title.istitle())
print(title2.istitle())
print("----------- in -----------")
print("Easy" in title)
print("Python" not in title)

