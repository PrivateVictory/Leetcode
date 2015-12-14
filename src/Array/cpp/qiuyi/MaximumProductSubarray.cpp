class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        int pMax = 0;
        int nMax = 0;
        int ret = INT_MIN;
        
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] < 0)
                swap(pMax, nMax);
            pMax = max(pMax*nums[i], nums[i]);
            nMax = min(nMax*nums[i], nums[i]);
            ret = max(ret, pMax);
        }
        
        return ret;
    }
};