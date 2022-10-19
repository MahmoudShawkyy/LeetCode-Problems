class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        answer=0
        check=False
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                answer+=1
                check=True
            elif check:
                break
        return answer
                
        