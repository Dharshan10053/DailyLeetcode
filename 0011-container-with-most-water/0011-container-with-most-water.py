class Solution(object):
    def maxArea(self, height):
        water=0
        i=0
        j=len(height)-1
        while j>i:
            water=max(water,min(height[i],height[j])*(j-i))
            if height[i]>height[j]:
                j-=1
            else:
                height[i]<height[j]
                i+=1
            
        return water
        