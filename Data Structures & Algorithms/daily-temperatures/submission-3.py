class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack =[]

        """
        [30,38,30,36,35,40,28]

        stack -> bottom to top
        [(30, 0), (38, 1)]

        [1,4,1,2,1,0,0]

        """

        stack = []
        result = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            while len(stack) > 0 and temperature > stack[-1][0]:
                popped_temp, popped_index = stack.pop()
                result[popped_index] = index - popped_index

            stack.append([temperature, index])
        
        return result
