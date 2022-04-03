class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq=[]
        for i in range(-100000,100000):
            freq.append(0)
        for i in range(len(nums)):
            freq[nums[i]]+=1
        for i in range(-100000,100000):
            if freq[i]==1:
                return i
            
        