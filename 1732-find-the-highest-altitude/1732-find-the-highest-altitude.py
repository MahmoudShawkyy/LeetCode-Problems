class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current=0
        answer=0
        for i in gain:
            current+=i
            answer=max(answer,current)
        return answer
        
        