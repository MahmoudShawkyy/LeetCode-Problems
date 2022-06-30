class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine=list(magazine)
        ransomNote=list(ransomNote)
        for char in ransomNote:
            if  not char in magazine:
                return False 
            magazine.remove(char)
        return True
        