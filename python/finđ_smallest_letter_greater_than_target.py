class Solution(object):
    def nextGreatestLetter(self, letters, target):
        left = 0
        right = len(letters) - 1
        while  left <= right:
            mid = (left+right) // 2 
            if letters[mid] <= target:
                left = mid + 1 
            else:
                right = mid - 1
        if left == len(letters):
            return left[0]
        else:
            return letters[left]
        
        
if __name__ in "__main__":
    s = Solution()
    s.nextGreatestLetter(letters = ["a","b","c"],target = "b")
    print(s)