#include <algorithm>
#include <cctype>
class Solution {
public:
    bool isPalindrome(string s) {
        if (s.empty())
            return true;
        
        s.erase(remove_if(s.begin(), s.end(),
            [](unsigned char c){return !isalnum(c);}), s.end());
        
        return std::equal(s.begin(), s.begin()+s.size()/2, 
                s.rbegin(), [](unsigned char a, unsigned char b){
                    return tolower(a)==tolower(b); 
                });
    }
};
