class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        answer=0
        for string in sentences:
            words=string.split()
            answer=max(answer,len(words))
        return answer