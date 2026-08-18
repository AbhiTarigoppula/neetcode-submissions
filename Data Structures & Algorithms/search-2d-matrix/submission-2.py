class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == target:
        #             return True

        # return False


        """
        matrix = [[1,2,4,8] 0 top
                  [10,11,12,13] 1
                  [15,20,30,40]] 2 bot

        target = 14

        top = 2
        bot = 1
        
        """

        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows - 1

        while top <= bot:
            mid_row = top + (bot - top) // 2

            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            else:
                break

        if top > bot:
            return False


        """
        10 11 12 13
        l  m  t
                 h

        target = 12

        """
        mid_row = top + (bot - top) // 2
        low, high = 0, cols - 1
        while low <= high:
            mid_value = low + (high - low) // 2
            if matrix[mid_row][mid_value] < target:
                low = mid_value + 1
            elif matrix[mid_row][mid_value] > target:
                high = mid_value - 1
            else:
                return True

        return False



