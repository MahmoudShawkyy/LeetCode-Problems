class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=-1
        for c in s:
            if c in t[i+1:]:
                i=t.index(c,i+1)
            else:
                return False
        return True
        