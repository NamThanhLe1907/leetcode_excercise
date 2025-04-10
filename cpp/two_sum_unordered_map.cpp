#include <vector>
#include <iostream>
#include <unordered_map>


class Solution {
public:
   std::vector<int> twoSUM(std::vector<int>&nums, int target) {
        std::unordered_map<int,int> my_dict;
        for (int i=0;i < nums.size();i++){
            int need = target - nums[i];
            if (my_dict.count(need)){
                return {my_dict[need],i};
            } 
            my_dict[nums[i]] = i;
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