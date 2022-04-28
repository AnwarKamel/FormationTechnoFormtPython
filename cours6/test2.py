def sum(numbers):
    total = 0
    for x in numbers:
        total = total + x
    return total

def multi(numbers):
    total = 1
    for x in numbers:
        total = total * x
    return total

list_numbers = [8, 2, 3, 1, 7]

result1 = sum((list_numbers))
result2 = multi((list_numbers))

print(f"Result = {result1}")
print(f"Result = {result2}")

