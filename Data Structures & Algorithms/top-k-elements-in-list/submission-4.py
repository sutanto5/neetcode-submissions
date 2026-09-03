class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # {number: freq}
        freq_count = {}

        # for loop getting each number
        for num in nums:
            if num in freq_count:
                freq_count[num] +=1
            else:
                freq_count[num] = 1
        
        # sort the dict
        sort_freq = dict(sorted(freq_count.items(), key = lambda x: x[1], reverse=True))

        return list(sort_freq.keys())[:k]