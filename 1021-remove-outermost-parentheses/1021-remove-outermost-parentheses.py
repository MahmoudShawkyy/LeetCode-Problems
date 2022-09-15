class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        temp=[]
        answer=[]
        counter=0
        for c in s:
            temp.append(c)
            if c=="(":
                counter+=1
            else:
                counter-=1
            if not counter:
                answer.extend(temp[1:-1])
                temp=[]
                
        return "".join(answer)
        