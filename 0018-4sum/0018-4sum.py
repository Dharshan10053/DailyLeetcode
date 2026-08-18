class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        fix1=nums[0]
        nums.sort()
        arr=[]
        for fix1 in range(len(nums)-3):
            for fix2 in range(fix1+1,len(nums)-2):
                left=fix2+1
                right=len(nums)-1
                while left<right:
                    total=nums[fix1]+nums[fix2]+nums[left]+nums[right]
                    if total==target and [nums[fix1],nums[fix2],nums[left],nums[right]] not in arr:
                        arr.append([nums[fix1],nums[fix2],nums[left],nums[right]])
                        left+=1
                        right-=1
                    elif total>target:
                        right-=1
                    else:
                        left+=1
        return arr

        