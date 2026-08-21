class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {} # num : count
        freq = [[] for i in range(len(nums) + 1)]

        # print(freq)

        for num in nums:
            map[num] = 1 + map.get(num, 0)
        
        # print(map)

        for num, count in map.items():
            freq[count].append(num)

        result = []
        for i in range(len(freq) - 1, -1, -1):
            for value in freq[i]:
                result.append(value)
                if len(result) == k:
                    return result