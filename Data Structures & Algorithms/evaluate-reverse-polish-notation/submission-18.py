class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ['+','-','*','/']

        for token in tokens:
            if token in operators:

                # get numbers
                num1 = stack.pop()
                num2 = stack.pop()

                # addition
                if token == '+':
                    stack.append(num1 + num2)

                # subtraction
                elif token == '-':
                    stack.append(num2 - num1)


                # multiplication
                elif token == '*':
                    stack.append(num1 * num2)

                # division
                else:
                    if num2 == 0:
                        stack.append(0)
                    else:
                        stack.append(int(num2 / num1))

            else:
                stack.append(int(token))
        return stack[0]

