class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer=[]
        temp=[]
        for i in range(0,len(nums),2):
            temp.append(nums[i]*[nums[i+1]])
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                answer.append(temp[i][j])
        return answer
        