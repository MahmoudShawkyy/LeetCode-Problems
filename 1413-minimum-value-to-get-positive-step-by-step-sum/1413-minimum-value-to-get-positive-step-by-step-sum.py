class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        presum=[]
        presum.append(nums[0])
        for i in range(1,len(nums)):
            presum.append(presum[i-1]+nums[i])
        if min(presum)>0:
            return 1
        else:
            return 1-min(presum)