class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right=0,1
        maxprof=0
        while  right < len(prices):
            if prices[left] < prices[right]:
                prof=prices[right]-prices[left]
                maxprof=max(prof,maxprof)
            else:
                left=right
            right+=1
        return maxprof