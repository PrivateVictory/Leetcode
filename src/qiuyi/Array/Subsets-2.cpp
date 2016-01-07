class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ret;
        vector<int> t;
        dfs(ret, t, nums, 0);
        return ret;
    }
    
    void dfs(vector<vector<int>>& ret, vector<int>& t, vector<int>& nums, int index) {
        ret.push_back(t);
        for (int i = index; i < nums.size(); i++) {
            if (i > index && nums[i] == nums[i-1])
                continue;
            t.push_back(nums[i]);
            dfs(ret, t, nums, i+1);
            t.pop_back();
        }
    }
};