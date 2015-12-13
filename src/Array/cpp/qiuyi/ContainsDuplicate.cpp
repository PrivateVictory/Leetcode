// Solution 1
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> mapping;
        for (auto i : nums) mapping[i] = 0;
        
        for (auto i : nums) mapping[i] += 1; 
        for (auto i : nums)
            if (mapping[i] >= 2)
                return true;
        return false;
    }
};

// Solution 2
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
       return nums.size() > set<int>(nums.begin(), nums.end()).size();
    }
};