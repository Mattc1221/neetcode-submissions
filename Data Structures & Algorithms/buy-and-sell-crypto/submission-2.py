class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices) - 1
        minL, maxR = prices[l], prices[r]
        while l < r:
            l_diff = prices[l] - prices[l+1]
            r_diff = prices[r-1] - prices[r]
            if l_diff >= r_diff:
                l += 1
                minL = min(prices[l], minL)
            else:
                r -= 1
                maxR = max(prices[r], maxR)
        return maxR - minL