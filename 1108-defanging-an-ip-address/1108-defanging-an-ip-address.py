class Solution:
    def defangIPaddr(self, address: str) -> str:
        answer=""
        for c in address:
            if c=='.':
                answer+='[.]'
            else:
                answer+=c
        return answer
        