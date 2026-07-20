class Solution:
    def isValid(self, s: str) -> bool:
        start = ['(', '[','{']
        end = [')',']','}']

        curr = []

        for char in s:
            
            if char in start:
                curr.append(char)
            else:
                
                if not curr:
                    return False

                last_letter = curr.pop()
                #)
                if (char == ')' and last_letter != '(') or (char == ']' and last_letter != '[') or (char == '}' and last_letter != '{'):
                   return False

        if curr:
            return False
                
        return True