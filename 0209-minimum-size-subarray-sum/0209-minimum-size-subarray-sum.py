class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        csum=0
        minlen=len(nums)
        for right in range(len(nums)):
            csum+=nums[right]
            while csum>=target:
                length=right-left+1
                minlen=min(length,minlen)
                csum-=nums[left]
                left+=1
        
        if minlen==len(nums) and left==0:     
            return 0
        return minlen


            

