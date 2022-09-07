class Solution:
    def findLucky(self, arr: List[int]) -> int:
        values={}
        for num in arr:
            if num in values:
                values[num]+=1
            else:
                values[num]=1
        
        answer=0
        for num,value in values.items():
            if num == value:
                answer=max(answer,num)
        return answer or -1
        
        
        