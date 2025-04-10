#include <iostream>
#include <unordered_map>
#include <string>


class Solution {
    public:
        int romanToInt(std::string s) {
            std::unordered_map<char,int> roman_dict = {
                {'I', 1},
                {'V', 5},
                {'X', 10},
                {'L', 50},
                {'C', 100},
                {'D', 500},
                {'M', 1000},
            };
            int total = 0;
            for (int i =0; i< s.size();i++){
                if(i < s.size() -1 && roman_dict[s[i]] < roman_dict[s[i+1]]){
                    total -= roman_dict[s[i]];
                }
                else{
                    total += roman_dict[s[i]];        
                }
            }
            return total;
        } 
    };

int main(){

    Solution obj;
    std::string s;
    std::cin >> s;
    std::cout << obj.romanToInt(s) << std::endl;
}