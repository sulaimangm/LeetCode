class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        leastPrice = prices[0]
        totalProfit = 0
        for i in prices:
            leastPrice = min(leastPrice, i)
            temp = i - leastPrice
            if temp > profit:
                profit = temp
                totalProfit += profit
                leastPrice = i
                profit = 0
        return totalProfit