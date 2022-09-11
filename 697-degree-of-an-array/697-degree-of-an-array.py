class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq=defaultdict(list)
        for i,n in enumerate(nums):
            freq[n].append(i)
        degree=max([len(x) for x in freq.values()])
        answer=len(nums)
        for index in freq.values():
            if len(index)==degree:
                answer=min(answer,index[-1]-index[0])
        return answer+1
                
        
                