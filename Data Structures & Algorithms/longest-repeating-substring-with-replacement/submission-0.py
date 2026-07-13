class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

       # AAABABB 

        start = 0
        
        hashMap = {}

        maxLen = 0

        for end in range(len(s)):
            hashMap[s[end]] = 1 + hashMap.get(s[end], 0)
            
            # insert new letter into hash map
            while (end - start + 1) - max(hashMap.values()) > k:
                hashMap[s[start]] -= 1
                start += 1
            
            maxLen = max(maxLen, end - start + 1)

        return maxLen
                #count of greatest char
            
            

         