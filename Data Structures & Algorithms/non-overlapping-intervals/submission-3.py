class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # case len 1:
        if len(intervals) < 2:
            return 0

        intervals.sort()
        
        curr = 0

        count = 0

        while curr < len(intervals) - 1:
            print(intervals)
            if intervals[curr][1] > intervals[curr+1][0]:
                #overlap
                
                endTime = min(intervals[curr+1][1], intervals[curr][1])
                
                count = count + 1
                
                if endTime == intervals[curr][1]:
                    intervals.remove(intervals[curr+1])
                else:
                    intervals.remove(intervals[curr])
            
            else:
                curr = curr + 1
                


               
                

        return count