class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # clean string
        cleaned = s.lower()

        
        front, end = 0, len(cleaned)-1

        while front < end:
            while not cleaned[front].isalnum() and front < end:
                front+=1

            while not cleaned[end].isalnum() and end > front:
                end-=1
           
            if cleaned[front] != cleaned[end]:
                return False
            else:
                front+=1
                end-=1

               
        
        return True

            