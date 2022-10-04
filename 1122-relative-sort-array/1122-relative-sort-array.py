class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        answer=[]
        for n in arr2:
            for k in arr1:
                if k==n:
                    answer.append(k)
        temp=sorted(arr1[len(arr2):])
        for i in range(len(temp)):
            if temp[i] not in arr2:
                answer.append(temp[i])
        return answer