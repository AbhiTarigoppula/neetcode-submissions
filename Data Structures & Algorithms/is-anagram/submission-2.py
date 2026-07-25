class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map = {}
        # First go through one string and sort each letter into its 'bucket'
        for letter in s:
            map[letter] = map.get(letter, 0) + 1 # same thing as .getOrDefault()
        
        # Second go through each letter in t and check if the bucket has a letter in it
        for letter in t:
            if letter not in map or map[letter] == 0:
                return False
            
            map[letter] -= 1
        
        
        return True
