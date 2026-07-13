class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two poniters at both ends
        left = 0
        right = len(heights) - 1

        area = 0

        while(left < right):
            curr = min(heights[left], heights[right]) * (right - left)

            if curr > area:
                area = curr

            if heights[left] > heights[right]:
                right = right - 1
            else:
                left = left + 1


        #if incrementing by one 
        return area

    
