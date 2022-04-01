
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp=[]
        for m in range(len(nums)):
            temp.append(nums[m])
        temp.sort()
        i=0
        j=len(nums)-1
        sum=temp[i]+temp[j]
        while sum!=target:
            if sum>target:
                j-=1
            elif sum<target:
                i+=1
            else:
                break
            sum=temp[i]+temp[j]
        first=temp[i]
        second=temp[j]
        ans=[]
        for k in range(len(nums)):
            if nums[k]==first:
                ans.append(k)
        for k in range(len(nums)):
            if nums[k]==second:
                ans.append(k)
        ans.sort()
        for k in range(len(ans)-2):
            if ans[k]==ans[k+1]:
                del(ans[k+1])
     
        return ans
            