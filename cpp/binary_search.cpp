#include <iostream>
#include <vector>


class Solution {
public:
    int search(std::vector<int>& nums, int target){
        int left = 0;
        int right = nums.size()-1;
        while (left <= right){
            int mid = (left + right) / 2 ;
            if (nums[mid] == target){
                return mid;
            }
            else if (nums[mid] < target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
            
        } 
        return -1;

    }

};

int main() {
    Solution obj;
    std::vector<int> arr = {-1, 0, 2, 3, 5, 7, 8, 10};
    int target = 5;
    int result = obj.search(arr, target);

    if (result != -1) {
        std::cout << "Found target at index " << result << std::endl;
    } else {
        std::cout << "Target not found!" << std::endl;
    }

    return 0;
}