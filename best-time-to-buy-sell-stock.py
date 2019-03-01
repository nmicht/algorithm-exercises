# 121 https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# SOLVED
# Dynamic programming

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        profit = 0
        i = 0

        if size >= 1:
            buy = prices[i]

            while i < size - 1:
                i += 1
                sell = prices[i]
                profit = max(sell-buy, profit)
                buy = min(sell, buy)

        return profit