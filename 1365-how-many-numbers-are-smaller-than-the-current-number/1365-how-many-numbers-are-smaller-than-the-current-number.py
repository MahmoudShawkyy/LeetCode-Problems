class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer=[]
        temp=nums.copy()
        nums.sort()
        for n in temp:
            answer.append(nums.index(n))
        return answer
            
        