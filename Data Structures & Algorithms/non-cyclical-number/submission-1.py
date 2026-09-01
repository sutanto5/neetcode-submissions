class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)

        while n != 1:
            summ = 0
            n = str(n)
            #square each digit
            for i in range(len(n)):
                summ = int(n[i]) * int(n[i]) + summ
            
            if summ in seen:
                return False
            
            else:
                seen.add(summ)
                n = summ
        
        return True
        

            