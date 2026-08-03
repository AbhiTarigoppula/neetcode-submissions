class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # This stores the number and its occurences
        freq = [[] for i in range(len(nums) + 1)]
        # [[], [], [], [], [], [4, 5]]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
            # print(count)
        
        for num, c in count.items():
            freq[c].append(num)
        
        res = []
        for num in range(len(freq) - 1, 0, -1):
            for value in freq[num]:
                res.append(value)
                if len(res) == k:
                    return res
        
