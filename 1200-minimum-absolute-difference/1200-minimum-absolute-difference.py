class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        values=[]
        for i in range(len(arr)-1):
            values.append(arr[i+1]-arr[i])
        values.sort()
        answer=[]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] == values[0]:
                answer.append([arr[i],arr[i+1]])
        return answer
                                     
        