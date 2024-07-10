class Solution:
    def minOperations(self, logs):
        stack=[]
        for ele in logs:
            if ele == "../":
                if stack :
                    stack.pop()
            elif ele == "./":
                continue
            else:
                stack.append(ele)
        return len(stack)