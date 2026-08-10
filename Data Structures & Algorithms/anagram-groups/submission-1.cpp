#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramMap;
        for(const string& str: strs){
            string key = str;
            sort(key.begin(), key.end());
            anagramMap[key].push_back(str);
        }
        vector<vector<string>> res;
        for(auto& pair: anagramMap)
            res.push_back(pair.second);
        return res;
    }
};
