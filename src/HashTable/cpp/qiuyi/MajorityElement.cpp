// Solution 1
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> count;
        for (auto i : nums)
            if (++count[i] > nums.size()/2)
                return i;
    }
};

// Solution 2
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate=0, cnt=0;
        for (auto i : nums)
            cnt == 0 ? candidate = i, cnt++ : i == candidate ? cnt++ : cnt--;
        return candidate;
    }
};