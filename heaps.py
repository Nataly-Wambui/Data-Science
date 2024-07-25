import heapq

#Create an empty list to represent the heap
min_heap = []

#Add elements to the heaap
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 9)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 4)
print(min_heap)

#Removing the smallest element
smallest= heapq.heappop(min_heap)
print(smallest)
print(min_heap)

#Converting the list into a heap
heapq.heapify(min_heap)
print(type(min_heap))

#Returning the smallest element in a heap
print(min_heap[0])

#Replacing the smallest element
heapq.heapreplace(min_heap, 7)
print(min_heap)

#Push and pop in one operation
heapq.heappushpop(min_heap, 6)
print(min_heap)

#Retrieving the smallest and largest elements
two_smallest = heapq.nsmallest(2, min_heap)
print(two_smallest)

two_largest = heapq.nlargest(2, min_heap)
print(two_largest)

#Implementing priority queues
assignments = [(4, 'assignment4'), (2, 'assignment2'), (3, 'assignment3'), (1, 'assignment1')]
print(assignments)
heapq.heapify(assignments)
print(assignments)
while assignments:
    print(heapq.heappop(assignments))

#Merging multiple sorted lists
multiple_lists = [[1,2,3,4,5], [5,6,8,9], [4,6,8,9]]
merged = []





