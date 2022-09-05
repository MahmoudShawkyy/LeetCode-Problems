class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        r=len(grid)
        l=len(grid[0])
        i=0
        j=l-1
        answer=0
        while i<r and j>=0 :
            if  grid[i][j]<0:
                answer+=r-i
                j-=1
            else:
                i+=1
        return answer