class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        result = 0

        for num in nums:
            if (num - 1) not in numSet:
                length = 1
                current_num = num
                while (current_num + 1) in numSet:
                    length += 1
                    current_num += 1

                result = max(length, result)

        return result