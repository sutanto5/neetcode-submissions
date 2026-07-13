class Solution:
    def isPalindrome(self, s: str) -> bool:
        #O(n) use two pointers to compare every element at the front and back to each other
        front = 0
        
        word = ""
        
        #remove alll non alphanumeric
        for char in s:
            if char.isalnum():
                word += char

        word = word.lower()
        back = len(word) - 1

        while(front < back):
            
            if(word[front] != word[back]):
                
                return False
            front = front + 1
            back = back - 1

        return True

        