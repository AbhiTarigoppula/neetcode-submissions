class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}

        if len(s) != len(t):
            return False

        for letter in s:
            map[letter] = map.get(letter, 0) + 1
        
        # print(map)

        for letter in t:
            if letter not in map or map[letter] == 0:
                return False
            
            map[letter] -= 1

        return True

