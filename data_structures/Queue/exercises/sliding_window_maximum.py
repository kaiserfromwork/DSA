from collections import deque
import random

sliding_window_examples = (
    ([1, 3, -1, -3, 5, 3, 6, 7], [3, 3, 5, 5, 6, 7]),  
    ([10, 5, 2, 7, 8, 7], [10, 7, 8, 8]),  
    ([4, 3, 5, 4, 3, 3, 6, 7], [5, 5, 5, 4, 6, 7]),  
    ([9, 7, 2, 4, 6, 8, 1, 5], [9, 7, 6, 8, 8, 8]),  
    ([11, 3, 7, 8, 15, 2, 6, 9], [11, 8, 15, 15, 15, 9]),  
    ([5, 1, 3, 9, 6, 4, 8, 7], [5, 9, 9, 9, 8, 8]),  
    ([20, 18, 16, 14, 12, 10, 8], [20, 18, 16, 14, 12]),  
    ([2, 9, 4, 1, 7, 3, 8, 5], [9, 9, 4, 7, 7, 8]),  
    ([7, 4, 6, 2, 9, 1, 5, 3], [7, 6, 6, 9, 9, 5]),  
    ([15, 10, 12, 8, 6, 20, 25, 18], [15, 12, 12, 20, 25, 25])  
)


# Selecting a random list 
my_list, expected_output = sliding_window_examples[random.randint(0, len(sliding_window_examples) - 1)]
print(my_list)

# Window size 
window_size = 3
window = deque()

result = []

for number in my_list:
   window.append(number)
   if len(window) == window_size:
      print(window)
      result.append(max(window))
      window.popleft()
      
print(f"Result: {result}")
print(f"Is it correct? {result == expected_output}")        