class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        nums = [1,2,2,3,3,3], k = 2

        1 1
        2 2
        3 3

        [2, 3]
        """


        # for num in nums:
        #     map[num] = map.get(num, 0) + 1
    
        # # print(map)

        # arr = []

        # for num, count in map.items():
        #     arr.append([count, num])
        # arr.sort()

        # result = []
        # while len(result) < k:
        #     result.append(arr.pop()[1])
        # return result

        map = {} # num : count
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            map[num] = 1 + map.get(num, 0)
        
        # print(map)

        for num, count in map.items():
            freq[count].append(num)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
