class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=["-1"]
        for i in s:
            if i in stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack[1::])
        
