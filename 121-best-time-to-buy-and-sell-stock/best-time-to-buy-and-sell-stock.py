class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minimum = prices[0]
        for i in range(len(prices)):
            if(prices[i]<minimum):
                minimum = prices[i]
            temp = prices[i]-minimum
            if(temp > profit):
                profit = temp
        return profit