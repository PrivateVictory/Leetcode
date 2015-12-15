class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ret;
        vector<int> t;
        dfs(ret, nums, t, 0);
        return ret;
    }
    
    void dfs(vector<vector<int>>& ret, vector<int>& nums, vector<int>& t, int index) {
        ret.push_back(t);
        for (int i = index; i < nums.size(); i++) {
            t.push_back(nums[i]);
            dfs(ret, nums, t, i+1);
            t.pop_back();
        }
    }
};