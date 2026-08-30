class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)

            add=0
            while n>0:
                digit=n%10
                add+= digit**2
                n=n//10
            
            n=add
        else:
            return True
        
