class Solution:
    #in: s -> lowercase letters
    def partitionLabels(self, s: str) -> List[int]:

        if len(s) == 0:
            return [0]

        #ret: [len(substring])]
        
        #xyxxy zbzbb isl
         #            ^ ^

        #count the freq 

        #abcabc
        #  ^  ^

        #count the frequencies

        #{letter: freq}
        freq = {}

        for letter in s:
            if letter in freq:
                freq[letter] = freq[letter] + 1
            else:
                freq.update({letter: 1})


        #now we have the frequencies
        res = []
        curr_letters = []
        length = 0
        for letter in s:
            length = length + 1
            #once all letters are 0 -> then we append to res
            if letter not in curr_letters:
                #append newly seen letters of subsring
                curr_letters.append(letter)
            
            #update freq
            freq[letter] = freq[letter] - 1
            
            #if last occurence then pop
            if freq[letter] == 0:
                curr_letters.remove(letter)
            
            #after pop -> chcek if 
            if len(curr_letters) == 0:
                
                res.append(length)
                length = 0
        
        return res



