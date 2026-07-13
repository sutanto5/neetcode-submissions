#include <string>

class Solution {
public:
    bool isPalindrome(string s) {
        std::string alpha_num;

        //remove Special characters
        for (int i = 0; i < s.size(); i++) {

            if(std::isalnum(s[i])){
                alpha_num.push_back(std::tolower(s[i]));
            }
        } 

        int ind1 = 0;
        int ind2 = alpha_num.length() - 1;
        std::cout << alpha_num <<std::endl;
        while(ind1 < ind2) {
            
            if (alpha_num[ind1] != alpha_num[ind2]) {
                return false;
            }
            ind1 +=1;
            ind2 -=1;
        }

        return true;
    }
};
