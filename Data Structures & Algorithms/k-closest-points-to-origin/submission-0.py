class Solution:
    def distance(self, x1: int, x2: int, y1: int, y2: int) -> float:
        return math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2) )
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #hashmap/dict containing all the points + distances {distance: point}
        closest = []
        
        for point in points:
            dist = self.distance(point[0], 0, point[1], 0)
        
            closest.append([-dist, point[0], point[1]])

            if len(closest) > k:
                heapq.heapify(closest)
                heapq.heappop(closest)
            
        res = []
        
        for tup in closest:
            dist, x, y = tup
            res.append([x, y])
        return res