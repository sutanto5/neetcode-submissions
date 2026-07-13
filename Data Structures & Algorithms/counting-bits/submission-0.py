class Solution:
    def countBits(self, n: int) -> List[int]:
        # n = 4 -> for loop from every number up to n
        
        #using the bin(num) -> can convert each number to binary

        #how to count the ones -> >>

        print("n = " + str(n))
        print("binary = " + bin(n))

        output = []
       

        for i in range(0, n+1):
            print(str(i))
            output.append(str(bin(i)).count("1"))

        return output