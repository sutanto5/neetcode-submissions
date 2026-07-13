class MinStack:

    def __init__(self):
        self.arr = []
        self.ordered = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.ordered.append(val)
        

    def pop(self) -> None:
        self.ordered.remove(self.arr[len(self.arr) - 1])
        
        self.arr.pop()

    def top(self) -> int:
        return self.arr[len(self.arr)-1]

    def getMin(self) -> int:
        heapq.heapify(self.ordered)
        print(self.arr)
        print(self.ordered)
        return self.ordered[0]
        
