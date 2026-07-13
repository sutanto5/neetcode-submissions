class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        #keep track of where we are at in the array
        start = 0
        end = 0

        #keeps track of letters in new iteration {letter, index}
        letters = {}

        #append 0 and 1

        #My Solution:
            #Continue incrementing end till we find a letter that is the same
                #keep track of characters by appending to hash map/dict -> O(1) lookup
                #if dupe is found I then want to increment the start to 1 after the index of dupe
                #continue till end reaches the last char

        #run through each letter in the string
        while end < len(s):
     
            
            letter = s[end]
            ind = letters.get(letter)
            

            if ind != None and ind >= start:
                #scootch window to 1 after dupe letter
                start = ind + 1

            
            letters.update({letter : end})
            #gonna updat here for now O(1)
            longest = max(end - start + 1, longest)

            end = end + 1
            
        return longest


