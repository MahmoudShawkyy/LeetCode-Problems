class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        answer=0
        n1=len(num1)-1
        n2=len(num2)-1
        for c in num1:
            answer+=(ord(c)-48)*(10**n1)
            n1-=1
        for c in num2:
            answer+=(ord(c)-48)*(10**n2)
            n2-=1
        return str(answer)