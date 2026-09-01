class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #g: integer array digits
        #   each digit is the digit of a large integer

        #return the full number plus one
        
        #rule: 
            #you always want to start with the last digit of the array
            #if that digit is 9 then move to the next digit
            #if the addition carries over to the msb then insert a 1 to extend the array

        #add 1 to the last bit:
            #while th bit = 9 then add to the next bit:
                #make this bit 0 and hte next bit add 1

        index = len(digits) - 1

        if digits[index] == 9:

            #find the bit to add the 1 to
            while digits[index] == 9 and index > -1:
                digits[index] = 0
                index = index - 1

            #check if index = 0
            if index == -1:
                #add teh carried over 1
                digits.insert(0, 1)
            else:
                 digits[index] = digits[index] + 1
            

        else:
            digits[index] = digits[index] + 1
        
        return digits
