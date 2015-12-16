class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> count;
        for (auto i : nums)
            if (++count[i] > nums.size()/2)
                return i;
    }
};