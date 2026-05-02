from collections import defaultdict
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize a dictionary to store the frequency of each number. 
        # defaultdict(int) automatically initializes any new missing keys with a value of 0.
        d = defaultdict(int)
        
        # Iterate through the input list and count the occurrences of each number.
        for num in nums:
            d[num] += 1 
            
        # Initialize a min-heap to keep track of the top 'k' elements. 
        # In Python, heapq creates a min-heap, and we will store lists in the format [frequency, number].
        heap = []
        
        # Iterate through the frequency dictionary (key = number, value = frequency)
        for key, value in d.items():
            # Optimization: Only push to the heap if we haven't reached 'k' elements yet,
            # OR if the current number's frequency is greater than the lowest frequency currently in the heap (heap[0][0]).
            if len(heap) < k or value > heap[0][0]:
                # Push the element. We put 'value' (frequency) first so the heap sorts by frequency.
                heapq.heappush(heap, [value, key])
            
            # If the heap size exceeds 'k', pop (remove) the element with the lowest frequency.
            # This ensures we only ever hold the top 'k' most frequent elements seen so far.
            if len(heap) > k:
                heapq.heappop(heap)
        
        # After evaluating all numbers, the heap contains exactly the 'k' most frequent elements.
        # We use a list comprehension to extract and return just the numbers (i[1]), discarding the frequencies.
        return [i[1] for i in heap]

        