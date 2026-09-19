from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        q=deque()
        for i,j in enumerate(tickets):
            q.append((i,j))
        count=0
        
        while q:
            person,remaining=q.popleft()
            remaining-=1
            count+=1
            if person==k and remaining==0:
                break
            if remaining>0:
                q.append((person, remaining))
        return count

        
