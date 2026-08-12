class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        prefix = 1
        for num in range(len(nums)):
            res[num] = prefix
            prefix *= nums[num]

        # print(res)

        postfix = 1
        for num in range(len(nums) - 1, -1, -1):
            res[num] *= postfix
            postfix *= nums[num]
        
        return res

