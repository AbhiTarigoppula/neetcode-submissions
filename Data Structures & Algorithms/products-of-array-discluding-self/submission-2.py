class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # res = [0] * n

        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
                
        #         prod *= nums[j]

        #     res[i] = prod
        # return res

        res = [0] * len(nums)

        prefix = 1
        for num in range(len(nums)):
            res[num] = prefix
            prefix *= nums[num]
        
        postfix = 1
        for num in range(len(nums) - 1, -1, -1):
            res[num] *= postfix
            postfix *= nums[num]
        
        return res
