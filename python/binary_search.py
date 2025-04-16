class Solution(object):
    def search(self, nums, target):
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else :
                    right = mid - 1
            return -1           
if __name__ == "__main__":
    s = Solution()
    arr = [-1,0,3,4,6,8,9]
    target = 6
    s.search(arr,target)