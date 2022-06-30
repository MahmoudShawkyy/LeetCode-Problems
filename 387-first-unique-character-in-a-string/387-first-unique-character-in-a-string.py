class Solution:
    def firstUniqChar(self, s: str) -> int:
        alpha={}
        for i in s:
            alpha[i]=0
        for i in s:
            alpha[i]+=1
        for i in s:
            if  alpha[i]==1:
                return s.index(i)
        return -1
        