class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        temp1=0
        temp2=0
        for c in range(k):
            temp1=0
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    temp2=grid[i][j]
                    grid[i][j]=temp1
                    temp1=temp2
            grid[0][0]=temp1
        return grid
                