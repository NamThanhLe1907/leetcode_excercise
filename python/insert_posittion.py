class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left += 1
                return left + 1 
            else:
                right -= 1
                return right + 1
                
            