class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """

        strs = ["act","pots","tops","cat","stop","hat"]

        act

        a - a = 0

        0   1   2 ... 
        [1], [], [] ...

        map -> key is ascii values and value is the word lists

        """

        map = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1

    
            # print(count)
            map[tuple(count)].append(word)

        return list(map.values())
