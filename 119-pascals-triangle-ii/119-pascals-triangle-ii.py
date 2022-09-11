class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal=[]
        pascal.append([1])
        for i in range(1,rowIndex+1):
            pascal.append([1]*(i+1))
        for i in range(len(pascal)):
            for j in range(1,len(pascal[i])-1):
                pascal[i][j]=pascal[i-1][j-1]+pascal[i-1][j]
        return pascal[rowIndex]
            
        
        
        