class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for letter in s:
            if letter == ")":
                temp=[]
                while stack[-1] != "(" :
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(letter)
        return "".join(stack)