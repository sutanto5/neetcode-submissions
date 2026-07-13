class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        #not enough gas to complete whole circuit
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        index = 0

        #find max diff
        for i, (x, y) in enumerate(zip(gas, cost)):
            total = total + x - y
            if total < 0:
                total = 0
                
                index = i + 1
        
        return index
