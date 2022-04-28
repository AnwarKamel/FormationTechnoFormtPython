f = open("file.txt")
f2 = open("file2.doc", "a+")
f2.write("Hello I am File 2dd")
f2.close()
print(f.read())
f2 = open("file2.doc", "r")

print(f2.read())


