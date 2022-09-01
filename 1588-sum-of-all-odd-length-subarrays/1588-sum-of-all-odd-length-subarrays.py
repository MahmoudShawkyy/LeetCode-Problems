class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        step=1
        answer=0
        temp=[]
        x=ceil(len(arr)/2)
        while x>0:
            i=0
            while step+i<=len(arr) :
                for j in range(i,i+step):
                    temp.append(arr[j])
                answer+=sum(temp)
                temp.clear()
                i+=1
            step+=2
            x-=1
        return answer
                    
                