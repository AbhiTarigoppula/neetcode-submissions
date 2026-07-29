class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Since we are trying to get the total profit we can iterate
        through each number and find the lowest possible price.
        
        Then the other case if finding the profit so then we can 
        take the price and subtract it from the minimum price we
        looked at and assign THAT number to max_profit and return it
        
        """

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        

        return max_profit