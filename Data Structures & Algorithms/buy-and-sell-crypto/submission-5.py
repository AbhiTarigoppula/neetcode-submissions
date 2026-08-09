class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_price = float('inf')
        # max_profit = 0

        # for price in prices:
        #     if price < min_price:
        #         min_price = price
        #     elif price - min_price > max_profit:
        #         max_profit = price - min_price

        # return max_profit

        low = 0
        high = 1
        maxP = 0

        while high < len(prices):
            if prices[low] < prices[high]:
                profit = prices[high] - prices[low]
                maxP = max(profit, maxP)
            else:
                low = high
            high += 1

        return maxP

