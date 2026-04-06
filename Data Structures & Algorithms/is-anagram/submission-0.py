class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Check if lengths match
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        # Step 2: Build frequency maps
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Step 3: Compare frequencies
        for c in countS:
            # We check if the count of character 'c' in S 
            # matches the count of 'c' in T
            if countS[c] != countT.get(c, 0):
                return False

        return True