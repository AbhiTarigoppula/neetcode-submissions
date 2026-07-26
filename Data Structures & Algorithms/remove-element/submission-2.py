class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        """

        have a variable as a "checker" that says if the number we are looking at is equal
        to the number we are looking FOR then we swap

        """

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        

        return k