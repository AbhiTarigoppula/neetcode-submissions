class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        s = "zxyzxyz"

        zxyzxyz
           l
              r

        set = {x, y}
        length = max(length, len(set)) 3, 2
        length = 3

        """

        # my_set = set()
        # left = 0
        # result = 0

        # for r in range(len(s)):
        #     # if the window is invalid we move l and valid move r
        #     while s[r] in my_set:
        #         my_set.remove(s[left])
        #         left += 1
        #     my_set.add(s[r])
        #     result = max(result, len(my_set))


        # return result'

        my_set = set()
        left = 0
        right = 0
        result = 0

        while right < len(s):
            if s[right] not in my_set:
                my_set.add(s[right])
                result = max(result, len(my_set))
                right += 1
            else:
                my_set.remove(s[left])
                left += 1
        
        return result











