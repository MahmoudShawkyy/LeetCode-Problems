class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        check=True
        num=[]
        while x!=0:
            num.append(x%10)
            x=x//10
        i=0
        j=len(num)-1
        while i<len(num)//2:
            if num[i]!=num[j]:
                check=False
                break
            i+=1
            j-=1
        return check