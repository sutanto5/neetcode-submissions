class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #goal: groups of groupsize size consecutively increasing numbers -> hand
            #return true -> if it is possible

        #check if we have the right amount of cards
        if len(hand) % groupSize != 0:
            return False
        
        #1, 2, 4, 2, 3, 5, 3, 4 -> not already sorted

        #1. sort the hand array -> O(n log n) -> due to pythhon sort function


        #2. Go through each group and check if each number is increasing by 1 -> O(n)

        #once we finish
        freq = {}
        minimum = float('inf')

        #get freq of each value -> by going through array and adding to dict
        for num in sorted(hand):
            #does key exist?
            if num in freq:
                #increment freq
                freq[num] = freq[num] + 1

            else:
            #maintain minimum value -> make sure to get
                freq[num] = 1
                minimum = min(minimum, num)

        #remove items till there is nothing left
        while len(freq) != 0:
            for i in range(0, groupSize):
                curr = minimum + i
                print(curr)
                if curr in freq:
                    freq[curr] = freq[curr] - 1
            
                    if freq[curr] == 0:
                        del freq[curr]

                    print(freq)

                else:
                    return False
            
            #update starting point of next group
            minimum = next(iter(freq.keys()), None)
            print(minimum)
                
        
        #then remove each number till num is not found or all numbers are in groups of consecutive numbers -> O(n)
        #curr = minimum
        return True

        