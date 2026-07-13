class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #there is always a unique answer
        #return x most frequent elements in an array

        #res -> k values
        #frequency of the elements

        #map - { number value: frequency} -> O(n)
        freq = {}

        #track frequencies
        for num in nums:
            #checking if num is a key
            if num in freq:
                #increment the value 
                freq[num] = freq[num] + 1
            else:
                freq.update({num : 1})

        #run through the map key, values plug in the k most frequent elements -> O(n)
        res = [] # -> keeps track of element val
        
        count = 0
        #run through sorted map
        for elmnt, frequ in sorted(freq.items(), key=lambda item: item[1], reverse = True):
            if len(res) < k:
                res.append(elmnt)


        return res

        