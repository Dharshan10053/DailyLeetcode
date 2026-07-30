class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        order=[]
        arr=[]
        result=[]
        miss=0
        
        for i in range(len(grid)):
            order.extend(grid[i])
        arr=sorted(list(set(order)))
        n=len(order)
        sum1=sum(arr)
        sum2=sum(order)
        miss=(n*(n+1)//2)-sum1
        rep=sum2-sum1
        return rep,miss

        

        
        
        