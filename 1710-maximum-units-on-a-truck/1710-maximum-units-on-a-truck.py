class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        temp=[]
        for i in range(len(boxTypes)):
                temp.append([boxTypes[i][1],boxTypes[i][0]])
        temp.sort(reverse=True)
        sum=0
        for i in range(len(temp)):
            for j in range(temp[i][1]):
                if truckSize:
                    sum+=temp[i][0]
                    truckSize-=1
                else:
                    break
        return sum
        
        