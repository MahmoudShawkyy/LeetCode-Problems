class Solution:
    def maxDepth(self, s: str) -> int:
        answer=0
        temp=0
        for c in s:
            if c=='(':
                temp+=1
                answer=max(answer,temp)
            elif c==')':
                temp-=1
        return answer
        