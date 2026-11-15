class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Hash Map {key : value} --> {char : freq}
        s_freq = {}
        for character in s:
            if character in s_freq:
                s_freq[character] += 1
            else:
                s_freq[character] = 1
        
        t_freq = {}
        for character in t:
            if character in t_freq:
                t_freq[character] += 1
            else:
                t_freq[character] = 1

        return t_freq == s_freq
        

