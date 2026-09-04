class Solution:
    def minimumSteps(self, s: str) -> int:
        s=list(s)
        p1=0
        count=0
        for p2 in range(len(s)):
            if s[p2]=='0':
                s[p1],s[p2]=s[p2],s[p1]
                count+=p2-p1   
                p1+=1
        return count
         
        
