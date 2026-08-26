import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        def distance(x1, x2, y1, y2):
            
            diff_x = x1 - x2
            diff_y = y1 - y2

            diff_x = math.pow(diff_x, 2)
            diff_y = math.pow(diff_y, 2)

            return math.sqrt(diff_x + diff_y)

        
        # build max heap of k size if anything less than current top -> pop and add new point
        # each element in the heap should be a tuple -> (distance, point)
        distances = []

        # O(n log n)
        for point in points:
            dist = distance(point[0], 0, point[1], 0)

            if len(distances) == k:

                if dist < abs(distances[0][0]):
                    heapq.heappop(distances)
                    heapq.heappush(distances, (-dist, point))

            else:    
                heapq.heappush(distances, (-dist, point))
        
        res = []
        for point in distances:
            res.append(point[1])

        return res

