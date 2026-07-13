class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #check s2 for any permutations of s1 exist within it

        #1. store every permutation of s1 -> and look for it in s2 -> O(2^n)
            #nested function -> dfs to find every permutation

        #2. create a window the size of s1 and check for every letter in s1 within that window O(n)
            #how to keep track of dupes -> s1 = aaa but the window is s2 = bab
            #freq of each char

        s1_freq = {}

        #get the character frequencies of s1
        for char in s1:
            if char not in s1_freq:
                s1_freq.update({char: 1})
            else:
                s1_freq[char] = s1_freq[char] + 1

        print(s1_freq)

        #

        #get the initial frequencies of s2
        s1_len = len(s1)
        
        #curr marker
        left = 0
        right = 0

        s2_freq = {}
       

        while right < len(s2):
            #not enough char in freq
            if right < s1_len:
                s2_freq[s2[right]] = s2_freq.get(s2[right], 0) + 1
            #window is the size of the s1
            else:
                #get the left character
                char = s2[left]
                #subtract the left character cuz were shifting the window
                s2_freq[char] = s2_freq[char] - 1

                #delete zeroes
                if s2_freq[char] == 0:
                    del s2_freq[char]

                left = left + 1

                if s2[right] in s2_freq:
                    s2_freq[s2[right]] = s2_freq[s2[right]] + 1
                else:
                    s2_freq.update({s2[right]: 1})

            right = right + 1

            if s2_freq == s1_freq:
                return True

            print(s2_freq)
            print(s2[left:right])
            print(left)
            print(right)
            
            
            


        return False