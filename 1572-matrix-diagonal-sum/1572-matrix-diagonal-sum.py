class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        answer=0
        for i in range(0,len(mat),1):
            answer+=mat[i][i]
        for i,j in zip(range(len(mat)-1,-1,-1), range(len(mat))):
            answer+=mat[j][i]
        if len(mat)%2!=0:
            n=len(mat)//2
            answer-=mat[n][n]
            
        return answer
            
        