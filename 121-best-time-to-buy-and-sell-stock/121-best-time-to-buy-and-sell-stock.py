class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start=prices[0]
        ans=0
        for i in range(1,len(prices)):
            if prices[i]<start:
                start=prices[i]
            else:
                ans=max(ans,prices[i]-start)
            
        return ans
        