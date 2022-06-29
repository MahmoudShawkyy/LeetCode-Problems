class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        if numRows>2:
            ans.append([1,1])
        for i in range(1,numRows):
            arr=[1]
            for j in range(1,i):
                arr.append(ans[i][j-1]+ans[i][j])
            arr.append(1)
            ans.append(arr)
            
        if len(ans)>2:
            del(ans[1])
        return ans