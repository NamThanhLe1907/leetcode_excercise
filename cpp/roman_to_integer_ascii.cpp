#include <iostream>
#include <string>



class Solution {
    public:
        int romanToInt(std::string s) {
            int roman[256] = {}; // ascii table
            roman['I'] = 1;
            roman['V'] = 5;
            roman['X'] = 10;
            roman['L'] = 50;
            roman['C'] = 100;
            roman['D'] = 500;
            roman['M'] = 1000;
    
            int total = 0;
            for (int i = 0; i < s.size(); i++) {
                if (i < s.size() - 1 && roman[s[i]] < roman[s[i + 1]]) {
                    total -= roman[s[i]];
                } else {
                    total += roman[s[i]];
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