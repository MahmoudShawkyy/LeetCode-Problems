class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        answer=0
        for word in words:
            counter=0
            for char in word:
                if char not in allowed:
                    break
                else:
                    counter+=1
            if counter==len(word):
                answer+=1
        return answer