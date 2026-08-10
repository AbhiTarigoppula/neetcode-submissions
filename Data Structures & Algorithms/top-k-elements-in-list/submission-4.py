class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        
        nums = [1,2,2,3,3,3], k = 2

        c: 1 2 3
        n: 1 2 3

        [2, 3]


        map = count : num
        
        result(end).append(2, 3)
        return result
        """

        map = {}
        freq = [[] for i in range(len(nums) + 1)]
        # [], [], []

        for num in nums:
            map[num] = 1 + map.get(num, 0)
        
        # print(map)

        for num, count in map.items():
            freq[count].append(num)

        result = []
        for index in range(len(freq) - 1, 0, -1):
            for num in freq[index]:
                result.append(num)
                if k == len(result):
                    return result