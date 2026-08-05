class Solution(object):
    def maxArea(self, height):
        area=0
        maxarea=0
        i=0
        j=len(height)-1
        while j>i:
            area=min(height[i],height[j])*(j-i)
            if area>maxarea:
                maxarea=area
            if height[i]>height[j]:
                j-=1
            elif height[i]<height[j]:
                i+=1
            else:
                i+=1
                j-=1
            
        return maxarea
        