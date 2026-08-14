class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][0]:
                popped_temp, popped_index = stack.pop()
                result[popped_index] = (index - popped_index)
            stack.append([temp, index])

        return result