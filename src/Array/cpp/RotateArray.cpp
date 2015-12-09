class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if (nums.empty() || k == 0) return;
        int j = 0, start = 0, moved = 0, temp = nums[0], len = nums.size();

        while (++moved <= len) {
            j = (j + k) % len;
            swap(temp, nums[j]);
            if (j == start) {
                j = ++start;
                temp = nums[j];
            }
        }
    }
};