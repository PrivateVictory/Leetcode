class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ret;
        vector<int> nums;
        sort(candidates.begin(), candidates.end());
        dfs(ret, nums, 0, candidates, target);
        return ret;
    }
    
    void dfs(vector<vector<int>>& ret, vector<int> nums, int index, vector<int>& candidates, int target) {
        if (target < 0)
            return;
        if (target == 0) {
            ret.push_back(nums);
            return;
        }
        for (int i = index; i < candidates.size(); i++) {
            nums.push_back(candidates[i]);
            dfs(ret, nums, i, candidates, target-candidates[i]);
            nums.pop_back();
        }
    }
};