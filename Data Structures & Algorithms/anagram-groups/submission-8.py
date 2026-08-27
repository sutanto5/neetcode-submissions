class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # arr : index in res
        freq_map = {}
        res = []

        curr_ind = 0

        for word in strs:

            # set up the alphabet arr
            freq_arr = [0] * 26

            for letter in word:
                # ord gets unicode numbering of letter
                index = ord(letter) - ord('a')
                freq_arr[index] += 1
            
            if tuple(freq_arr) not in freq_map:
                res.append([word])
                freq_map[tuple(freq_arr)] = curr_ind
                curr_ind+=1
            
            else:
                index = freq_map[tuple(freq_arr)]
                curr_words = res[index]
                curr_words.append(word)
                res[index] = curr_words

        return res


        
