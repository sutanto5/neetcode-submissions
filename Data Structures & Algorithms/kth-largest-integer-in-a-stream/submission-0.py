import heapq

class KthLargest:


    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums
        

    def add(self, val: int) -> int:
        #need to implement max heap not min heap
        self.arr.append(val)
        
        heapq.heapify(self.arr)
        largest = heapq.nlargest(self.k, self.arr)

        return largest[self.k - 1]

