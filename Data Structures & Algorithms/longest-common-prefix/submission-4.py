class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """

        the first word will be our prefix
        the length will be the length of the first word
        
        Then iterate through each string and if the word we are looking at is greater than 
        the prefix's length we decrease prefix

        """

        prefix = strs[0]
        length = len(strs[0])

        for word in strs:
            while prefix[0:length] != word[0:length]:
                length -= 1

        return prefix[:length]