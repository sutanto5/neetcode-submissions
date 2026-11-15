class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # map {letter : frequency}
        return sorted(s) == sorted(t)
