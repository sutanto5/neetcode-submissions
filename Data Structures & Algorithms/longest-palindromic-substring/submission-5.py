class Solution:
    def longestPalindrome(self, s: str) -> str:
        resInd = 0
        resLength = 0

        currLength = 1
        currInd = 0


        def checkPalindrome(left, right):
            nonlocal currLength
            nonlocal currInd

            while left >= 0 and right < len(s) and s[left] == s[right]:
                currLength += 2
                left -= 1
                right += 1

            currInd = left + 1
                

        # i is the center
        for i in range(len(s)):
            left = i - 1
            right = i + 1

            if i + 1 < len(s) and s[i] == s[i+1]:
                currLength = 2
                checkPalindrome(left, right + 1)
            
            if currLength >= resLength:
                resInd = currInd
                resLength = currLength
                currLength = 1
            else:
                currLength = 1
            
            checkPalindrome(left, right)

            #check index and length
            if currLength >= resLength:
                resInd = currInd
                resLength = currLength
                currLength = 1
            else:
                currLength = 1
                
        
        return s[resInd: resInd + resLength]



        


        
