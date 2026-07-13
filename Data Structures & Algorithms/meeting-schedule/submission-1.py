"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        intervals.sort(key=lambda i: i.start)

        minStart = float("-inf")
        maxStart = float("-inf")

        for point in intervals:
            if point.start < maxStart:
                return False
            else:
                minStart = point.start
                maxStart = point.end

        
        return True

    
        