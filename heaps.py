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




##How do you find the smallest k elements in an array using a heap?
def smallest_k_elements(arr, k):
    return heapq.nsmallest(k, arr)

print(smallest_k_elements([2,5,6,7,2,1,8,9], 3))

##How do you implement a priority queue using a heap?
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        return heapq.heappush(self.heap, (priority, item))

    def pop(self):
        return heapq.heappop(self.heap)[1]

    def peek(self):
        return self.heap[0][1] if self.heap else None

    def is_empty(self):
        return len(self.heap) == 0


##How do you find the kth smallest element in a matrix sorted row-wise and column-wise?
def kth_smallest(matrix, k):
    n = len(matrix)
    min_heap = []
    for r in range(min(n, k)):  
        heapq.heappush(min_heap, (matrix[r][0], r, 0))

    number = 0
    for _ in range(k):
        number, r, c = heapq.heappop(min_heap)
        if c + 1 < len(matrix[0]):
            heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
            
    return number
print(kth_smallest([[1, 5, 9],[10, 11, 13],[12, 13, 15]], 8))


## How do you find the maximum sum of a sliding window of size k using a heap?
def max_sliding_window(nums, k):
    if not nums:
        return []

    max_heap = []
    result = []
    for i in range(len(nums)):
        heapq.heappush(max_heap, (-nums[i], i))
        if i >= k - 1:
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            result.append(-max_heap[0][0])  

    return result
print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))

## How do you find the median of a stream of numbers using heaps?
class MedianFinder:
    def __init__(self):
        self.max_heap = []  
        self.min_heap = []  

    def add_num(self, num):
        heapq.heappush(self.max_heap, -num)
        if (self.max_heap and self.min_heap and 
            (-self.max_heap[0] > self.min_heap[0])):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2



