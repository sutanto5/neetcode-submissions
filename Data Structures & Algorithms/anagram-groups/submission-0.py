

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #best would be O(n) time where n is the size of array
        
        #make a map of index values where the key is the anagram
        anagrams = {}
        
        #want to iterate through all strings
        for i, word in enumerate(strs):

            word = strs[i]
            key = sorted(word)
            key = "".join(key)

            #if not in anagram
            res = anagrams.get(key)
            print(res)
            print("current map: " + str(anagrams))
            if  res == None:
                anagrams.update({key:[word]})
            else:
                res.append(word)
                anagrams[key] = res
        
        results = list(anagrams.values())

        return results

        