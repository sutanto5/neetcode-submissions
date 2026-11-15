class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Hash Map {key : value} --> {char : freq}

        # check for invalid char
        if len(s) != len(t):
            return False

        # O(n)
        s_freq = {}
        for character in s:
            if character in s_freq:
                s_freq[character] += 1
            else:
                s_freq[character] = 1
        
        t_freq = {}
        # O(m)
        for character in t:
            if character in t_freq:
                t_freq[character] += 1
            else:
                t_freq[character] = 1

        # match keys and look at their values
        return t_freq == s_freq

        # time complexity: O(n + m)
        # space complexity: O(n + m) -> but since we have 26 character max -> O(1)
        

