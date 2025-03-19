# Queues - First In First Out (FIFO)

from collections import deque

q = deque()

print(q)

# Enqueue - Add element to the right o(1)
q.append(1)
q.append(3)
q.append(4)
q.append(6)

print(q)

# Dequeue (pop from the left) - Remove element from the left side O(1)
q.popleft()

print(q)


# Peek from left (FIRST INDEX) - O(1) 
print(q[0])

# Peek from right (LAST INDEX) - O(1)
print(q[-1])