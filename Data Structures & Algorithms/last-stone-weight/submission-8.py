class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        if len(heap) >= 2:
            while len(heap) > 1:
                x = abs(heapq.heappop(heap))
                y = abs(heapq.heappop(heap))

                if x > y:
                    x = x - y
                    heapq.heappush(heap, -x)
                elif x < y:
                    y = y - x
                    heapq.heappush(heap, -y)



            
        if len(heap) == 0:
            return 0
        else:
            return -heap[0]