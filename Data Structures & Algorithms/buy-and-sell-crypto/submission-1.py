class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        max_score = -9999999
        for price in prices:
            mini = min(mini, price)
            max_score = max(price - mini, max_score)
        return max_score
