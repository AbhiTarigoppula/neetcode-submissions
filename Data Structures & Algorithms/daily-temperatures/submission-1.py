class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack =[]

        """
        [30,38,30,36,35,40,28]

        stack -> bottom to top
        [(30, 0), (38, 1)]

        """

        for index, temp in enumerate(temperatures):
            while len(stack) != 0 and stack[-1][0] < temp:
                popped_temp, popped_index = stack.pop()
                result[popped_index] = (index - popped_index)
            
            stack.append([temp, index])
        
        return result
