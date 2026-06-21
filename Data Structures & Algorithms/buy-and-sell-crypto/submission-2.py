class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices): #reached the last element
            #print (prices[l],prices[r])
            profit = prices[r] - prices[l]
            
            maxProfit = max(maxProfit, profit, maxProfit)
            print(prices[l], prices[r], profit,maxProfit)
            # want left to be low
            # want right to be high
            if (prices[l+1] < prices[l]) and (l+1) < r:
                l += 1
            elif (prices[r] < prices[l]):
                l = r
                r = r + 1
            else:
                r += 1
        
        return maxProfit