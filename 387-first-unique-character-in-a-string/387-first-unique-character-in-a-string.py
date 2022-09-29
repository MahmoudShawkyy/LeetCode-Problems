class Solution:
    def firstUniqChar(self, s: str) -> int:
        answer={}
        for c in s:
            if c in answer:
                answer[c]+=1
            else:
                answer[c]=1
        for i,c in enumerate(s):
            if answer[c]==1:
                return i
        return -1