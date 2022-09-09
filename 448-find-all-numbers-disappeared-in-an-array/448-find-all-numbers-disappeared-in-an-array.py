class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        values=[0]*(len(nums)+1)
        answer=[]
        for i in range(len(nums)):
            values[nums[i]]=1
        for i in range(1,len(values)):
            if values[i]==0:
                answer.append(i)
        return answer