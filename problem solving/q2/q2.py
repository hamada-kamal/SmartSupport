'''
************************* exeplanations **********************
the method uses nested loops to compare each element in the list with the elements that come after it.
it checks if the price of the later element is greater than the price of the earlier element.
if it is, it calculates the difference between the two prices and compares it with the current 
maximum profit. If the difference is greater, it updates the maximum profit.
'''
class Solution:
    def __init__(self,pris):
        self.prices =pris
    profit = 0
    def maxProfit(self,prices):
        for a in range(len(prices)):    
            for i in range(a,len(prices)):
                if prices[i] > prices[a] and prices[i] - prices[a] > self.profit:
                    self.profit = prices[i] - prices[a]
        return self.profit


#Test
prices = [7,1,5,3,6,4]
s = Solution(prices)

print(s.maxProfit(s.prices))
