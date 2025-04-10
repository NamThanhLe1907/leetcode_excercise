#include <vector>
#include <iostream>

class Solution {
public:
   std::vector<int> twoSUM(std::vector<int>&nums, int target) {
        for (int i=0;i < nums.size();i++){
            for (int j=i+1;j < nums.size(); j++){
                if (nums[i]+nums[j] == target){
                       std::cout << "[" << i << "," << j << "]" << std::endl;
                       return {i,j};
                    }
                }
            }
            return {};
        }
    }
;


int main() {
    Solution obj;

    std::vector<int> nums = {2,5,6,4,3,1};
    int target = 9;
    
    obj.twoSUM(nums,target);
    
}