from collections import deque
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        count=0
        stack=[]
        for i in range(len(sandwiches)-1,-1,-1):
            stack.append(sandwiches[i])
        q=deque()
        for i in range(len(students)):
            q.append(students[i])
        while q and count<len(q):
            if q[0]==stack[-1]:
                q.popleft()
                stack.pop()
                count=0 #reset
            else:
                q.append(q.popleft())
                count+=1
        return len(q)
