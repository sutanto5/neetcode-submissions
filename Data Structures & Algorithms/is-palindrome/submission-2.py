import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # case insensitive
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        x = list(s)

        front = 0
        back = len(x) - 1

        while front < back:
            print(x[front])
            print(x[back])
            if x[front] != x[back]:
                return False
            else:
                front += 1
                back -=1
        return True