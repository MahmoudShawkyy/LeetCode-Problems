class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp=[]
        for i in nums:
            temp.append(i)
        temp.sort()
        i=0
        j=len(nums)-1
        x=0
        y=0
        ans=[]
        while True:
            if temp[i]+temp[j]>target:
                j-=1
            elif temp[i]+temp[j]<target:
                i+=1
            else:
                x=temp[i]
                y=temp[j]
                break
                
        for i in range(len(nums)):
            if x==nums[i]:
                ans.append(i)
                break
                
        for i in range(len(nums)):
            if y==nums[i] and i!=ans[0]:
                ans.append(i)
                break
                
        return ans
                
        