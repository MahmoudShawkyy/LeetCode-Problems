class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max([num for num in arr if arr.count(num)==num],default=-1)
        
        
        