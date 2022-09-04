class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        arr = [[0]*n for i in range(m)]
        for index in indices:
            for i in range(n):
                arr[index[0]][i]+=1
            for j in range(m):
                arr[j][index[1]]+=1
        answer=0
        for i in range(m):
            for j in range(n):
                if arr[i][j]%2!=0:
                    answer+=1
    
        return answer
            
        