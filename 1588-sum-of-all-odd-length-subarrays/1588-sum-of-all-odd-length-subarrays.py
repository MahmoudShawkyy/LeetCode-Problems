class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sub=[]
        for i in range(1,len(arr)+1,2):
            for j in range(len(arr)+1-i):
                sub.append(arr[j:j+i])
        return sum(sum(s) for s in sub)
            
                    
                