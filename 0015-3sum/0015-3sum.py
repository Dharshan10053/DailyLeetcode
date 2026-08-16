class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        fix=-1
        arr=[]
        nums.sort()
        for i in range(fix+1,len(nums)):
            fix+=1
            left=i+1
            right=len(nums)-1
            
            while left<right:
                total=nums[right]+nums[left]+nums[fix]
                if total==0 and [nums[left],nums[right],nums[fix]] not in arr :
                    arr.append([nums[left],nums[right],nums[fix]])
                    left+=1
                    right-=1
                elif total>0:
                    right-=1
                else:
                    left+=1
        return arr
                
    

