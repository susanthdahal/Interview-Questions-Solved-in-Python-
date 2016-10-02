'''Find max profit for stock buy sell with a cool down'''

class Solution(object):

    def maxProfit(self,prices):
        if len(prices)<=1:
            return 0

        buy1=-prices[0]
        sell1=0
        sell2=0
        for i in range(1,len(prices)):
            buy=max(buy1,sell2-prices[i])
            sell=max(sell1,buy1+prices[i])
            buy1=buy
            sell2=sell1
            sell1=sell
        return sell1


obj=Solution()
print(obj.maxProfit([1, 2, 3, 0, 2]))
