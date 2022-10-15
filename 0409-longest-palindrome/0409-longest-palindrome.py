class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq={}
        for c in s:
            if c not in freq:
                freq[c]=1
            else:
                freq[c]+=1
        answer=0
        for key,value in freq.items():
            if freq[key]%2==0:
                answer+=freq[key]
            else:
                answer+=freq[key]-1
        if answer%2==0 and answer!=len(s):
            answer+=1

        
        return answer
        