#include <iostream>
#include <vector>



class Solution {
public:
    char nextGreatestLetter(std::vector<char>& letters, char target) {
        int left = 0;
        int right = letters.size() - 1 ;
        while (left <= right){
            int mid = (left+right) / 2;
            if (letters[mid] <= target){
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }
        }
        if (left == letters.size()){
            return letters[0];
        }
        else{
            return letters[left];
        }
        }
    
};

int main() {
    Solution obj;
    std::vector<char> letters = {'a','b','c'};
    char target = 'b';
    char results = obj.nextGreatestLetter(letters,target);

    std::cout << "Next char " << target << " is " << results << " " << std::endl;
    return 0;
}