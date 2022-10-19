class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer=""
        mini=min(strs)
        for i in range(len(mini)):
            c=strs[0][i]
            for s in strs:
                if s[i]!=c:
                    return answer
            answer+=c
        return answer