class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        temp=[]
        ans=[]
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                temp.append(mat[i][j])
        if r*c!=len(temp):
            return mat
        x=0    
        for i in range(r):
            arr=[]
            for j in range(c):
                arr.append(temp[x])
                x+=1
            ans.append(arr)
            
        return ans
                
                
                
            