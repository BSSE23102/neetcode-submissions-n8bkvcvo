from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            lst = [0]*26
            for char in word:
                lst[ord(char)-ord('a')] += 1
            # Tuples are immutable and hashable, making them valid dictionary keys
            lst = tuple(lst) 
            dic[lst].append(word)
            
        # Cast the dict_values view into a standard list
        return list(dic.values())