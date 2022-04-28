counter = 0
numbers = [0, 1, 2, 3, 4, 5, 6, 7]
for counter in numbers:
    counter += 1
    if counter == 3:
        continue
    print(counter)
