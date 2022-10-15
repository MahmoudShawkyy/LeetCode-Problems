class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        first,second={},{}
        for i,n in enumerate(list1):
            first[n]=i
        mini=2000
        for i,n in enumerate(list2):
            if n in first:
                second[n]=first[n]+i
                mini=min(mini,second[n])
        return [key for key,value in second.items() if value==mini]