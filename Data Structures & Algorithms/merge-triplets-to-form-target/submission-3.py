class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        #g: triples -> ai, bi, ci
        #   target = [x, y, z] -> goal

        #operations:
            #1. choose 2 triplets update triples[j] to become the max of both triplet vals
            #return true if it is get target or not

            [1, 2, 3]
            [7, 1, 1]

            [7, 2, 3]

            #all three target exist somewhere in triplets -> 

            [2, 5, 6]
            [1, 4, 4]
            [5, 7, 5]

            [5, 4, 6]

            #any target number cannot be minimum unless all three targets are already in triple

            

            [1, 5, 1]
            [5, 2, 3]
            [10, 10, 5]

            #none of these target values is the minimum -> values can be middle, but must not be next to other values taht are max of the other indexes


            #1. all three targets must exist
            #2. cannot be minimum value of a triplet[i]
            #3. if max value cannot take the triplet because no value will be lower

        #O(n)

        #for loop -> and by keeping track of the mi   
            a,b,c = target

            curr = [float('-inf'), float('-inf'), float('-inf')]

            for triple in triplets:

                #triple has all three
                if triple == [a, b, c]:
                    return True

                x, y, z = triple

                if x > a or y > b or z > c:
                    continue
                
                else:
                    curr = [max(curr[0], x), max(curr[1], y), max(curr[2], z)]
                    if curr == target:
                        print(curr)
                        return True
                


            return False


            


            
                
            



            
            



