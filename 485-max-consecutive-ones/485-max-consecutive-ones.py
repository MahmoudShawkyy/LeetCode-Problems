class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer=0
        summ=0
        for n in nums:
            if n==1:
                summ+=1
            else:
                summ=0
            answer=max(summ,answer)
        return answer
            
        