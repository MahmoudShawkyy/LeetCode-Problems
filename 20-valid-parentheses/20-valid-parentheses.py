class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        stack.append(s[0])
        for i in range(1,len(s)):
            if stack and stack[-1]=='(':
                if s[i]==')':
                    stack.pop()
                else:
                    stack.append(s[i])
            elif stack and stack[-1]=='{':
                if s[i]=='}':
                    stack.pop()
                else:
                    stack.append(s[i])
            elif stack and stack[-1]=='[':
                if s[i]==']':
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return  not len(stack)