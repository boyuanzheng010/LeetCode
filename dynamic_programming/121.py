"""
Greedy
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float('inf')
        best_profit = 0

        for price in prices:
            if price < mini:
                mini = price
                best_profit = best_profit - (mini - price)
            elif price - mini > best_profit:
                best_profit = price - mini
        return best_profit




















