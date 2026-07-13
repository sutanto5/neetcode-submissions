from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
       #best case diff lenghts
       if len(s) != len(t):
            return False

       #hash map of tuples
       freq_s = Counter(s)
       freq_t = Counter(t)
       
       return freq_s == freq_t
        