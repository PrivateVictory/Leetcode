class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = 0;
        int ret = -INT_MAX;
        
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            ret = max(sum, ret);
            if (sum < 0)
                sum = 0;
        }
        
        return ret;
    }
};