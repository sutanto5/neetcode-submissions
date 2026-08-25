import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)

        # create a max heap
        for i in range(n):
            stones[i] = -stones[i]

        heapq.heapify(stones)
        
        while len(stones) > 1:
            x = abs(heapq.heappop(stones))
            y = abs(heapq.heappop(stones))

            if x < y:
                y = y - x
                heapq.heappush(stones, -y)
            elif y < x:
                x = x - y
                heapq.heappush(stones, -x)
        
        if stones:
            return abs(stones[0])
        else:
            return 0
            

