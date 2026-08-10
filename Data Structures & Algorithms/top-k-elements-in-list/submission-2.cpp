#include <vector>
#include <array>
#include <algorithm>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::array<int, 2001> freq = {0};
        for(const int n:nums)
            freq[n+1000]++;

        vector<pair<int, int>> counts;
        counts.reserve(2001);
        for(int i=0; i<2001; i++)
        {
            if(freq[i]>0)
                counts.push_back({freq[i], i-1000});
        }
        
        sort(counts.begin(), 
        counts.end(),
        [](const auto&a, const auto&b){return a.first>b.first;});

        vector<int> res;
        res.reserve(k);
        for(int i=0;i<k;i++)
            res.push_back(counts[i].second);
        
        return res;
    }
};
