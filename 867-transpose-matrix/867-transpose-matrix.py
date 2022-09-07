class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        m=len(matrix[0])
        answer=[]
        for i in range(m):
            answer.append([])
            for j in range(n):
                answer[i].append(0)
        for i,k in zip(range(n),range(n)):
            for j,l in zip(range(m),range(m)):
                answer[j][i]=matrix[k][l]
        return answer
        