class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        one=[]
        for c in s:
            if one and c=='#':
                one.pop()
            elif c!="#":
                one.append(c)
        two=[]
        for c in t:
            if two and c=='#':
                two.pop()
            elif c!='#':
                two.append(c)
        return one==two
        