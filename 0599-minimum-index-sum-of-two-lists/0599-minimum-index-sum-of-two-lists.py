class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        val=2000
        pairs={}
        for i,n in enumerate(list1):
            for j,k in enumerate(list2):
                if n==k:
                    pairs[n]=j+i
                    val=min(val,j+i)
        answer=[]
        for key,value in  pairs.items():
            if value==val:
                answer.append(key)
        return answer
        