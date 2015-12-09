class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret;
        int sum;

        for (int j = nums.size()-1; j > 0; j--) {
            sum = nums[j];
            for (int i = 0; i < j; i++) {
                sum += nums[i];
                if (sum == target) {
                    ret.push_back(i+1);
                    ret.push_back(j+1);
                }
                else {
                    sum -= nums[i];
                }
            }
        }
        return ret;
    }
};