class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        result = 0
        my_set = set()

        while right < len(s):
            if s[right] not in my_set:
                my_set.add(s[right])
                right += 1
            else:
                my_set.remove(s[left])
                left += 1
            result = max(result, len(my_set))

        return result


