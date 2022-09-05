class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        answer=0
        for arr in grid:
            for i in arr:
                if i <0:
                    answer+=1
        return answer
        