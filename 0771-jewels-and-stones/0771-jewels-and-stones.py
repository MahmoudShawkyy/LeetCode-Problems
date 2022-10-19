class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer=0
        for j in jewels:
            for s in stones:
                if j==s:
                    answer+=1
        return answer