class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        index = len(intervals)

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                index = i
                break
        
        #check front interval
        if index != 0 and newInterval[0] <= intervals[index - 1][1]:
            end = max(newInterval[1], intervals[index - 1][1])
            newInterval[0] = intervals[index - 1][0]
            newInterval[1] = end
            intervals.pop(index - 1)
            index = index - 1
        
        while index < len(intervals) and newInterval[1] >= intervals[index][0]:
            newInterval[1] = max(newInterval[1], intervals[index][1])
            intervals.pop(index)
            print(intervals)

        intervals.insert(index, newInterval)

            

        
        return intervals
        