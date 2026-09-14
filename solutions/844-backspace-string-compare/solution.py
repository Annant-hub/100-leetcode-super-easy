class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=["-1"]
        stack2=["-1"]
        for i in s:
            if i=="#" and stack1[-1]=="-1":
                continue
            elif i=="#" and stack1[-1]!="-1":
                stack1.pop()
                
            else:
                stack1.append(i)
        for j in t:
            if j=="#" and stack2[-1]=="-1":
                continue
            elif j=="#" and stack2[-1]!="-1":
                stack2.pop()              
            else:
                stack2.append(j)
        if stack1==stack2:
            print(stack1,stack2)
            return True
        else:
            return False


            

