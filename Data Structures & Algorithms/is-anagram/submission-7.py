class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map = {}

        for letter in s:
            map[letter] = 1 + map.get(letter, 0)

        for letter in t:
            if letter not in map or map[letter] == 0:
                return False
            map[letter] -= 1

        return True