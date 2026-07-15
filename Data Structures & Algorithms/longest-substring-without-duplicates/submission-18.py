class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) < 1:
            return 0
        
        l, r = 0, 1
        longestSubstring = 1
        currLength = 1

        # map of {char: index}
        currChars = {}
        currChars[s[l]] = l

        while r < len(s):

            currRight = s[r]

            if currRight in currChars:

                l = max(l, currChars[currRight] + 1)
                
                while s[l] == currRight and l < r:
                    l = l + 1

                del currChars[currRight]

                longestSubstring = max(longestSubstring, currLength)
                print(currLength)
                currLength = r - l

            # add right value to arr
            currChars.update({currRight : r})
            currLength = currLength + 1

            # increment right val
            r = r + 1

        longestSubstring = max(longestSubstring, currLength)

        return longestSubstring
