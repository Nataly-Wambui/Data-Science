from collections import deque

#Add items in a queue
names = deque()
names.append("Nataly")
names.append("Wambui")
names.append("Ivy")
names.append("Akwang'")
names.append("Gitahi")
names.append("Mary")
print(names)
print(type(names))
names.appendleft("Lesley")
print(names)

#Remove items from a queue
names.pop()
print(names)
names.popleft()
print(names)

#Accessing items in a queue
names.insert(0, "Lesley")
print(names)
names.remove("Wambui")
print(names)
print(names.count("Nataly"))
print(len(names))

#Accessing the front and back element
print(names[0])
print(names[-1])


