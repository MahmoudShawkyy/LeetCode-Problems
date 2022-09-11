class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros=[]
        for i,n in enumerate(arr):
            if n==0:
                zeros.append(i)
        step=0
        for i in range(len(zeros)):
            if zeros[i]<len(arr)-1:
                arr.insert(zeros[i]+step,0)
                del(arr[-1])
                step+=1
            