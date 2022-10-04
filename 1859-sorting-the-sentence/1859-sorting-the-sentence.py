class Solution:
    def sortSentence(self, s: str) -> str:
        temp=s.split()
        answer=[""]*(len(temp))
        s=' '.join(temp)
        string=''
        for c in s:
            if c !=' ' and ord(c)>58:
                string+=c
            elif c !=' ':
                answer[int(c)-1]=string
                string=''
        return ' '.join(answer)