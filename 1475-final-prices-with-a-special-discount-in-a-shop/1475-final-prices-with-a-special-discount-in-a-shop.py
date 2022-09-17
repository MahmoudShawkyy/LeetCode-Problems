class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[]
        for i,n in enumerate(prices):
            while stack and prices[stack[-1]]>=n:
                prices[stack.pop()]-=n
            stack.append(i)
            
        return prices