class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        answer=0
        target=tickets[k]
        for i,n in enumerate(tickets):
            if i>k and n>=target:
                answer+=target-1
            elif n>=target:
                answer+=target
            else:
                answer+=n
        return answer
                
                
                