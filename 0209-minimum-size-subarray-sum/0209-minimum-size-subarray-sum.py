class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        csum=0
        minlen=len(nums)+1
        for right in range(len(nums)):
            csum+=nums[right]
            while csum>=target:
                minlen=min(right-left+1,minlen)
                csum-=nums[left]
                left+=1
        
        if minlen==len(nums)+1:     
            return 0
        return minlen


            

