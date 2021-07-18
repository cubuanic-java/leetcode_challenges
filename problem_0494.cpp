"""
This is a straight adaptation from the python implementation
Using maps instead of tabulation comes with a huge performance
Penalty
"""

using std::unordered_map;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) 
    {
        unordered_map<int, int> current_sum = {{0, 1}};

        for(auto const& num: nums) 
        {
            unordered_map<int, int> next;

            for (const auto& [key, val] : current_sum) 
            {
                next[key + num] += val;
                next[key - num] += val;
            }

            current_sum = next;
        }

        return current_sum[target];
    }
};