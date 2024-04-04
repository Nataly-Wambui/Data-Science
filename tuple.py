# creating a tuple
numbers= (2,3,4,5,6,7)
print(numbers)
print(type(numbers))

numbers = 2,3,4,5,6,7
print(numbers)

# Adding items to a tuple
newNumbers = list(numbers)
print(newNumbers)
print(type(newNumbers))
newNumbers.insert(2,9)
print(newNumbers)
numbers = tuple(newNumbers)
print(numbers)

# Changing items in a tuple
newNumbers = list(numbers)
print(type(newNumbers))
print
newNumbers[3]=8
print(newNumbers)
numbers = tuple(newNumbers)
print(numbers)

# Removing items from a tuple
newNumbers = list(numbers)
print(newNumbers)
print(type(newNumbers))
newNumbers.remove(7)
print(newNumbers)
numbers = tuple(newNumbers)
print(numbers)


