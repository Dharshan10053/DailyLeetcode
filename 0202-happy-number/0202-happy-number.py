class Solution(object):
    def isHappy(self, n):
        seen = set()
        last_digit=0
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            sum1=0
            while n!=0:
                last_digit=n%10
                sum1=sum1+last_digit**2
                n=n//10
            n=sum1
        return True
       
        
            
    
            
        