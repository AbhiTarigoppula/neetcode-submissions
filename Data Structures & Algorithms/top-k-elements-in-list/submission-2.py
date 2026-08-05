class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        nums = [1,2,2,3,3,3], k = 2

        1 1
        2 2
        3 3

        [2, 3]
        """

        map = {} # num : count

        for num in nums:
            map[num] = map.get(num, 0) + 1
    
        # print(map)

        arr = []

        for num, count in map.items():
            arr.append([count, num])
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        return result
