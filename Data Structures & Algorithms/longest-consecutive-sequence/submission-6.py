class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        result = 0

        for num in my_set:
            if (num - 1) not in my_set:
                length = 1
                current_num = num

                while (current_num + 1) in my_set:
                    length += 1
                    current_num += 1
                result = max(result, length)

        return result
