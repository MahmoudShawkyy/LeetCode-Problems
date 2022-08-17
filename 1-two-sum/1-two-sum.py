class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values={}
        for i in range(len(nums)):
            number=target-nums[i]
            if number in values:
                return [values[number],i]
            values[nums[i]]=i
            