class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i=0
        while i<=(x//2)+1:
            if i*i>x:
                return i-1
            elif i==x or i*i==x:
                return i
            else:
                i+=1
            
                
        