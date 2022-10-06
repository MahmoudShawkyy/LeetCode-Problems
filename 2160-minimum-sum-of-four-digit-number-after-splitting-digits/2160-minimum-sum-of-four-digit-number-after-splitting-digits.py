class Solution:
    def minimumSum(self, num: int) -> int:
        number=str(num)
        temp=list(number)
        nums=[]
        for i in range(len(temp)):
            nums.append(int(temp[i]))
        nums.sort()
        return (nums[0]+nums[1])*10+nums[2]+nums[3]