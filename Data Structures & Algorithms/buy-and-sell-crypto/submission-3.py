class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices): #reached the last element
            profit = prices[r] - prices[l]
            # want left to be low
            # want right to be high
            print(prices[l], prices[r], profit,maxProfit)
            
            if (prices[l] < prices[r]):
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
                #print(prices[l], prices[r], profit,maxProfit)
            else:
                l = r
                #print(prices[l], prices[r], profit,maxProfit)
            r += 1
        
        return maxProfit