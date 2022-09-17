class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer=[]
        check=True
        for i,n in enumerate(prices):
            check=True
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    answer.append(prices[i]-prices[j])
                    check=False
                    break
            if check:
                answer.append(prices[i])
            
        return answer