class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            
            y, x = heapq.nlargest(2, stones)
            stones.remove(x)
            stones.remove(y)
            

            if x < y:
                stones.append(y - x)
            print(stones)

        if len(stones) > 0:
            return stones[0]
        else:
            return 0