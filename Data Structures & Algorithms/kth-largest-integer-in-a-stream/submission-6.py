class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for num in nums:

            if len(self.heap) < k:

                heapq.heappush(self.heap,num)
            else:
                heapq.heappush(self.heap, num)
                heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        
        if len(self.heap) >= self.k:
            heapq.heappush(self.heap, val)
            heapq.heappop(self.heap)
        else:
            heapq.heappush(self.heap,val)


        print(self.heap)

        return self.heap[0]
        
