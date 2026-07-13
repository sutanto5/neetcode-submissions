class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #g: tokens -> a math expression

        #12+3*4-
       # 1 + 2 = 3 *3 = 9 - 4 = 5
        stack = []
       #stack problem -> where we are pushing numbers onto the stack till we find an operator
        for char in tokens:
        #the operator function

            if char in "+-/*":
                x1 = stack.pop()
                x2 = stack.pop()
                print(stack)
                 #calculate based on the operator and pop back onto the stack
                stack.append(self.calculate(x1, x2, char))

            #if its an operatoer
            else:
                stack.append(int(char))
                
                

               
            
        
        #there will only be one value in the stack left
        return stack[0]

    #this doesnt account for non valid values
    def calculate(self, x1, x2, operator):
        print(operator)
        print(x1)
        print(x2)
        if operator == '*':
            return x1 * x2
        
        elif operator == '/':
            return int(x2/x1)
        
        elif operator == '-':
            return x2 - x1
        
        #assume plus
        else:
            return x1 + x2